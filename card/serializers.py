from rest_framework import serializers
from .models import Card
from .validators import card_number_validate, card_verify_exist
from .token import Token


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'card_type', 'created_at', 'card_number']
        fields_read_only = ['card_number']

    def validate(self, data):
        """ Realiza as validações das requisições POST """
        card_number = data.get('card_number')
        if not card_number_validate(card_number):
            raise serializers.ValidationError({'card_number': 'Card number is invalid.'})
        
        if card_verify_exist(card_number):
            raise serializers.ValidationError({'card_number': 'Card number already registered'})

        return data

    def create(self, validated_data):
        """ Realiza a criação de um Card com número criptografado """
        card_number = validated_data.pop('card_number', None)
        if card_number is not None:
            token = Token()
            card_number_tokenized = token.tokenize(card_number)
            print('Token: ', card_number_tokenized)
            validated_data['card_number'] = card_number_tokenized
            
        return super().create(validated_data)


class CardSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id']

class FileSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ['file']

    def create(self, validated_data):
        return validated_data
