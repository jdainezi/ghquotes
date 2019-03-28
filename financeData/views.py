from django.shortcuts import render
from rest_framework import viewsets, filters, renderers
from financeData import models, serializers

# Create your views here.
class QuoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows currency quotations to be viewed.
    """
    queryset = models.CurrencyQuote.objects.all()
    serializer_class = serializers.QuoteSerializer
