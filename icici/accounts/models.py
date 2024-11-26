from django.db import models

# Create your models here.

class AccountOpeningModel(models.Model):
    refid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    DOR = models.DateField()
    mobile = models.BigIntegerField()
    count = models.IntegerField(auto_created=True)