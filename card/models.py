from django.db import models

class Card(models.Model):
    CARD_TYPES = (
        ('C', 'Credito'),
        ('D', 'Debito'),
    )

    card_type = models.CharField(max_length=1, choices=CARD_TYPES, default='C')
    card_number = models.CharField(max_length=250, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.card_number)
