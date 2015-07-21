from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=20)
	amount= models.FloatField(default=0.0)
	active = models.BooleanField(default=True)
	
	
#Method sira mak tuir mai ne'e:
	def __unicode__(self,):
			#import pdb
			#pdb.set_trace()
	     		return "{} {}'s:USD $.{}".format( self.name, self.user, self.amount)

	def __init__(self, *args, **kwargs):
             		super(Account, self). __init__( *args, **kwargs)
			if 'amount' in kwargs:
             			  self.amount = kwargs['amount']
			

        def add(self, value):
			super(Account,self). __init__( *args, **kwargs)
			
            		self.amount = self.amount + self.value
                        self.save()
			return self.amount
	     		
        def subtract(self, value):
		
             		self.amount = self.amount - value
	     		self.save()
	    
	     		return self.amount

        def interest(self, rate):
             		self.amount = self.amount + ( self.amount * rate/100.0)
	     		self.save()
             		return self.amount

        def compound_interest(self, rate, period):
			
             		self.amount = self.amount * (( 1 + rate/100.0) ** period)
	     		self.save() 
	     		return self.amount

        #def total_amount(self,):
             		#return  "USD ${0:.2f}".format(self.amount)

     	

     	


