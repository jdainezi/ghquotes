import requests, django, sys, os
sys.path.append(".")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")
django.setup()
from financeData.models import QuoteModel
import datetime

def _get_quotes_json():
    url = 'https://api.hgbrasil.com/finance'
    access_key = '56d386c5'
  
    r = requests.get('{0}?key={1}'.format(
        url, 
        access_key))

    try:
        r.raise_for_status()
        return r.json()
    except:
        return None
      
def update_quotes():
    json = _get_quotes_json()
    if json is not None:
        try:
            now = datetime.datetime.now()
            bitcoin = json['results']['currencies']['BTC']['buy']
            dolar = json['results']['currencies']['USD']['buy']
            euro = json['results']['currencies']['EUR']['buy']

            new_quotes = QuoteModel()
            new_quotes.bitcoin = bitcoin
            new_quotes.euro = euro
            new_quotes.dolar = dolar
            new_quotes.datetime = now

            new_quotes.save()
        except:
            pass


update_quotes()
