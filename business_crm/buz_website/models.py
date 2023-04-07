from django.db import models

# Create your models here.

class Customer(models.Model):
	
	name = models.CharField(max_length=60)
	age = models.CharField(max_length=60)

	
class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	birttday = models.CharField(max_length=30)
	sex = models.CharField(max_length=60)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=60)
	address = models.CharField(max_length=150)
	city = models.CharField(max_length=60)
	state = models.CharField(max_length=60)
	zipcode = models.CharField(max_length=60)


	def __str__(self):
		return (f"{self.first_name} {self.last_name}")
		
