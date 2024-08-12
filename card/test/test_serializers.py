from django.test import TestCase
from card.models import Card
from card.serializers import CardSerializer


class CardSerializerTestCase(TestCase):
    def setUp(self):
        self.card = Card(
            card_number='6513941382733774',
            card_type='C'
        )
        self.serializer = CardSerializer(instance=self.card)

    def test_verifica_campos_serializados(self):
        """ Teste para verificar os campos de serialização """
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'card_number', 'card_type', 'created_at'})

    def test_verifica_conteudo_dos_campos_serializados(self):
        """ Teste para verificar o conteúdo dos campos serializados """
        data = self.serializer.data
        self.assertEqual(data['card_number'], self.card.card_number)
        self.assertEqual(data['card_type'], self.card.card_type)


