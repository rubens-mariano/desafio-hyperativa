from rest_framework.test import APITestCase
from django.test import TestCase
from card.models import Card
from django.urls import reverse
from rest_framework import status


class CardModelTesteCase(TestCase):
    def setUp(self):
        self.card = Card(
            card_number='6513941382733774',
        )

    def test_verica_atributos_card(self):
        """ Teste de verificação dos atributos default de um Card """
        self.assertEqual(self.card.card_type, 'C')
        self.assertEqual(self.card.card_number, '6513941382733774')



# class CardsTestCase(APITestCase):
#     def setUp(self):
#         self.list_url = reverse('Cards-list')
#         self.card_1 = Card.objects.create(card_number='6513941382733774', card_type='C')
#         self.card_2 = Card.objects.create(card_number='4389359716551810', card_type='C')
#
#     def test_requisicao_get_para_listar_cards(self):
#         """ Teste para verificar a requisição GET para listar os cards """
#         response = self.client.get(self.list_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_requisicao_post_para_criar_card(self):
#         data = {
#             'card_number': '5041757234175052',
#             'card_type': 'C'
#         }
#
#         response = self.client.post(self.list_url, data=data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
