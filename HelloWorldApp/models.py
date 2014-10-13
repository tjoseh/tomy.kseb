from django.db import models

# Create your models here.

class Country(models.Model):
    name =  models.CharField(max_length =50)
    currency =  models.CharField(max_length =10)

class CountryNew(models.Model):
    name =  models.CharField(max_length =50)
    currency =  models.CharField(max_length =10)
    def __unicode__(self):
        return u'%s' % (self.name)
