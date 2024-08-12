from .models import Card


def digits_of(n):
    """ Busca e retorna o dígito de um número """
    return [int(d) for d in str(n)]


def card_number_validate(card_number):
    """ Algoritimo Luhn's para validação dos números de cartões """
    digits = digits_of(card_number)

    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]

    checksum_odd = sum(odd_digits)
    checksum_even = sum(sum(digits_of(d * 2)) for d in even_digits)

    is_valid = (checksum_odd + checksum_even) % 10 == 0
    return is_valid
