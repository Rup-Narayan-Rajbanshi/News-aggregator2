from django.db import models

# Create your models here.

class Message(models.Model):
	name=models.CharField(max_length=250)
	email=models.EmailField(null=True,blank=True)
	subject=models.CharField(max_length=1000,null=True,blank=True)
	message=models.TextField()
	