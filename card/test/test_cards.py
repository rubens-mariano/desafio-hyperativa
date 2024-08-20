from django.contrib.auth.models import User, Permission
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from card.models import Card
from card.token import Token


class CardsTesteCase(APITestCase):
    def setUp(self):
        self.card = Card.objects.create(card_number='5258858515633872', card_type='D')
        self.user = (User.objects.create_user('rubens', password='123456').
                     user_permissions.add(
            Permission.objects.get(codename='add_card'),
            Permission.objects.get(codename='change_card'),
            Permission.objects.get(codename='delete_card')
        ))
        self.list_url = reverse('Cards-list')
        self.token_url = reverse('token_obtain_pair')
        response = self.client.post(self.token_url, data={'username': 'rubens', 'password': '123456'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.access_token = response.data['access']

    def test_create_card(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        data = {'card_number': '4389354860325632', 'card_type': 'C'}
        response = self.client.post(self.list_url, data)
        card_number = response.data['card_number']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(card_number, '57cfa0bd39b925be769d3a5ee687029a6248c1fae18893650d2d34896f76557a')
        self.assertEqual(response.data['card_type'], 'C')

    def test_update_card(self):
        data = {
            'card_number': self.card.card_number,
            'card_type': 'C'
        }

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.put(reverse('Cards-detail', args=[self.card.id]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_card(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.delete(reverse('Cards-detail', args=[self.card.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_search_number_card(self):
        token = Token()
        card_number_tokenized = token.tokenize('4389354860325632')
        print(card_number_tokenized)
        print(Card.objects.all())
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(reverse('cards-search', args=['4389354860325632']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)




