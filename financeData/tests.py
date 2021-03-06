from django.test import TestCase
from financeData.models import QuoteModel
import datetime
import pdb

class QuoteTestCase(TestCase):
   
    def test_valid_quote(self):
        '''Tests if there is an empty value in the database model'''
        db = QuoteModel.objects
        inv_bitcoin = db.filter(bitcoin__gte=0)
        inv_dolar = db.filter(dolar__gte=0)
        inv_euro = db.filter(euro__gte=0)

        self.assertIsNot(inv_bitcoin, db.none(), msg='Found invalid bitcoin value entry')
        self.assertIsNot(inv_dolar, db.none(), msg='Found invalid dolar value entry')
        self.assertIsNot(inv_euro, db.none(), msg='Found invalid euro value entry')

    def test_input_schedule(self):
        '''Tests if the database has been updated hourly'''
        dblist = QuoteModel.objects.all()
        db = QuoteModel.objects
        skiped = None
        skiped_times = ''
        for i in range(len(dblist)-1):
             if getattr(db.get(pk=i+1),'datetime') - getattr(db.get(pk=i),'datetime') > datetime.timedelta(minutes=1,hours=1):
                skiped = 1
                skiped_times += ' ' + str(getattr(db.get(pk=i),'datetime'))
        self.assertIsNotNone(skiped, msg='Found moments when data was not parsed at {}'.format(skiped_times))
        





