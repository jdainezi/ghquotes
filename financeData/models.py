from django.db import models

# Create your models here.

class QuoteModel(models.Model):
    bitcoin = models.DecimalField(decimal_places=2,max_digits=8)
    dolar = models.DecimalField(decimal_places=2,max_digits=4)
    euro = models.DecimalField(decimal_places=2,max_digits=4)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.datetime)
