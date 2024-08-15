from django.db import models
from cryptography.fernet import Fernet, InvalidToken
from django.conf import settings


class Card(models.Model):
    CARD_TYPES = (
        ('C', 'Credito'),
        ('D', 'Debito'),
    )

    card_type = models.CharField(max_length=1, choices=CARD_TYPES, default='C')
    card_number = models.CharField(max_length=250, unique=True)
    created_at = models.DateField(auto_now_add=True)

    @property
    def card_number_decrypted(self):
        """ Realiza a descriptografia e retorna o do número do cartão """
        try:
            key = self.get_encryption_key()
            cipher_suite = Fernet(key)
            return cipher_suite.decrypt(self.card_number.encode()).decode('utf-8')
        except InvalidToken:
            raise InvalidToken("Invalid Token! Decryption failed.")

    def encrypt_card_number(self, card_number):
        """ Encripta o número do cartão e retorna o número do cartão encriptado """
        key = self.get_encryption_key()
        cipher_suite = Fernet(key)
        encrypted_card_number = cipher_suite.encrypt(card_number.encode('utf-8'))
        return encrypted_card_number

    def decrypted_card_number(self, card_number_encrypted):
        """ Realiza a descriptografia e retorna o do número do cartão criptografado informado por parâmetro """
        try:
            key = self.get_encryption_key()
            cipher_suite = Fernet(key)
            return cipher_suite.decrypt(card_number_encrypted.encode()).decode('utf-8')
        except InvalidToken:
            raise InvalidToken("Invalid Token! Decryption failed.")

    @staticmethod
    def get_encryption_key():
        """ Retorna o número da chave de criptografia """
        fernet_key = settings.FERNET_KEY
        return fernet_key

    def __str__(self):
        return str(self.card_number)
