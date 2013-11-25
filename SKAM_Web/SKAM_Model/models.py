from django.db import models

# Create your models here.

class Competitors(models.Model):
	teamname = models.CharField(max_length=50)
	ipaddress = models.CharField(max_length=20)
	

