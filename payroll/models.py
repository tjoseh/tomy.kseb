from django.db import models
from datetime import date
# Create your models here.

class Employe(models.Model):
    employe_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length =20,blank=False,null=False)
    last_name = models.CharField(max_length =20,blank=True,null=True)
    pan =  models.CharField(max_length =10,blank=False,null=False)
    dob = models.DateField()
    doj = models.DateField()
    bank_ac =  models.IntegerField()
    def __unicode__(self):
        return u'%s %s' % (self.first_name,self.last_name)
    

class Tax(models.Model):
    employe =  models.ForeignKey(Employe)
    month =  models.DateField()
    tax_amount = models.IntegerField(max_length=6)
    def __unicode__(self):
        return u'%s' % (self.tax_amount)

class Leave(models.Model):
    employe =  models.ForeignKey(Employe)
    from_date =  models.DateField()
    to_date =  models.DateField()

    
