from rest_framework import serializers
from .models import Card
from .validators import card_number_validate


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'card_type', 'created_at', 'card_number']
        fields_read_only = ['card_number']

    def validate(self, data):
        """ Realiza as validações das requisições POST """
        card_number = data.get('card_number')
        if not card_number_validate(card_number):
            raise serializers.ValidationError('Card number is invalid.')

        return data

    def create(self, validated_data):
        """ Realiza a criação de um Card com número criptografado """
        card_number = validated_data.pop('card_number', None)
        card = Card()
        if card_number is not None:
            encrypted_card_number = card.encrypt_card_number(card_number)
            validated_data['card_number'] = encrypted_card_number.decode()
        return super().create(validated_data)


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file',)

    def create(self, validated_data):
        return validated_data
