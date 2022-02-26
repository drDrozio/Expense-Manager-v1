from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    balance = models.IntegerField(default=0)

    def __str__(self):
	    return str(self.username)



class Expense(models.Model):
    CATEGORY = (
            ('Electricity','Electricity'),
            ('Food','Food'),
            ('Gifts','Gifts'),
			('Groceries','Groceries'),
            ('Miscellaneous','Miscellaneous'),
			('Recreations','Recreations'),
			('Rent','Rent'),
            ('Subscriptions','Subscriptions'),
            ('Transportation','Transportation'),
            ('Travel','Travel'),
            ('Water','Water'),
		)
    amount = models.IntegerField(default=0)
    description = models.TextField()
    category = models.CharField(max_length=255, choices=CATEGORY)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
	    return str(self.user.username) + '_' + str(self.category) + '_' + str(self.amount)
