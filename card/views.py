from io import BytesIO
from rest_framework import viewsets, status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Card
from .serializers import CardSerializer, FileSerializer, CardSearchSerializer
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
import pandas as pd
from .token import Token


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    http_method_names = ['post', 'put', 'push']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return self.build_response(serializer, request)

    def build_response(self, card_serializer, request):
        response = Response(card_serializer.data, status=status.HTTP_201_CREATED)
        location_url = self.build_location_url(card_serializer, request)
        response['Location'] = location_url
        return response

    @staticmethod
    def build_location_url(card_serializer, request):
        card_id = str(card_serializer.data['id'])
        return f"{request.build_absolute_uri()}{card_id}"


class CardSearchView(generics.ListAPIView):
    def get_queryset(self):
        token = Token()
        card_number_tokenized = token.tokenize(self.kwargs['card_number'])
        queryset = Card.objects.filter(card_number=card_number_tokenized)
        return queryset
    
    serializer_class = CardSearchSerializer


class CardFileProcessor:
    @staticmethod
    def process_card_file(file):
        """ Realiza a leitura e processamento dos dados do arquivo informado """
        file.seek(0)
        data = BytesIO(file.read())
        names_columns = ['LINE', 'CARD_NUMBER']
        df_cards = pd.read_fwf(
            data, header=None, skiprows=1, skipfooter=1,
            colspecs=[(0, 1), (7, 26)], engine='python',
            names=names_columns
        )
        return df_cards

    @staticmethod
    def include_cards(data_frame):
        """ Realiza a inclusão dos Cards através do CardSerializer e realiza a
        verificação dos Cards válidos e inválidos """
        for _, row in data_frame.iterrows():
            card_data = {'card_type': row['LINE'], 'card_number': row['CARD_NUMBER']}
            card_serializer = CardSerializer(data=card_data)
            if card_serializer.is_valid(raise_exception=True):
                card_serializer.save()
            else:
                return ValidationError(card_serializer.errors)


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        """ Realiza o upload do arquivo """
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            df_cards = CardFileProcessor.process_card_file(request.data['file'])
            try:
                CardFileProcessor.include_cards(df_cards)
            except ValidationError as e:
                return Response({'detail': str(e)}, status=400)

            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=400)
