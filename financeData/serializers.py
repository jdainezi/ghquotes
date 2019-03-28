from financeData.models import CurrencyQuote
from rest_framework import serializers

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyQuote
        fields = ('datetime','bitcoin','dolar','euro')
