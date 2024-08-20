from .models import Card
from .token import Token

def digits_of(n):
    """ Busca e retorna o dígito de um número """
    return [int(d) for d in str(n)]


def card_number_validate(card_number):
    """ Algoritimo Luhn's para validação dos números de cartões """
    digits = digits_of(card_number)

    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]

    checksum_odd = sum(odd_digits)
    checksum_even = sum(map(lambda d: sum(digits_of(d*2)), even_digits))
    

    is_valid = (checksum_odd + checksum_even) % 10 == 0
    return is_valid


def card_verify_exist(card_number):
    token = Token()
    card_number_tokenized = token.tokenize(card_number)
    is_valid = Card.objects.filter(card_number=card_number_tokenized).exists()
    return is_valid