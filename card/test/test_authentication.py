from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import authenticate
from django.urls import reverse


class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cards-list')
        self.user = User.objects.create_user('rubens', password='123456')
        self.token_url = reverse('token_obtain_pair')
        response = self.client.post(self.token_url, data={'username': 'rubens', 'password': '123456'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.access_token = response.data['access']

    def test_autenticacao_user_com_credenciais_corretas(self):
        """ Teste para verificar a autenticação de um usuário com credenciais corretas """
        user = authenticate(username='rubens', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_autenticacao_user_com_credenciais_incorretas(self):
        """ Teste para verificar a autenticação de um usuário com credenciais incorretas """
        user = authenticate(username='rubens', password='12345')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada_por_token(self):
        """ Teste para verificar uma requisição GET não autorizada por token incorreto """
        response = self.client.get(self.list_url, HTTP_AUTHORIZATION='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
                                                                     '.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMz'
                                                                     'Y0MDIwOCwiaWF0IjoxNzIzNDY3NDA4LCJqdGkiOiI5Y2JmZ'
                                                                     'jAzMmNhNWU0OTY4ODcyMzVlZTJkNmEzMmEwYSIsInVzZXJfa'
                                                                     'WQiOjF9.fPO669VOQm_h3U0l_JZqyghFzn6CaVcVSS'
                                                                     'Uupu7GX3g')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_requisicao_get_autorizada_por_token(self):
        """ Teste para verificar uma requisição GET autorizada por token """
        response = self.client.get(self.list_url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
