from django.db import models

"""
	@Table 	Competitor
	@Column Teamname ipaddress
	@ToDo	user input for iteration 2 for ipadress and teamname	
"""
class Competitors(models.Model):
	teamname = models.CharField(max_length=50)
	ipaddress = models.CharField(max_length=20)
	
"""
	@Table 	Service
	@Column servicename servicestatus
	@ToDo	read monitoring from here 
"""
class Services(models.Model):
	servicename = models.CharField(max_length=50)
	servicestatus = models.BooleanField()


