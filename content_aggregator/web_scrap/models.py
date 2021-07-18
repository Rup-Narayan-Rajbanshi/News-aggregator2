from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here
class Category(models.Model):
    category=models.CharField(max_length=250,null=True,blank=False)

    def __str__(self):
        return self.category


class Data(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    headline=models.CharField(max_length=1000,null=True,blank=True)
    url=models.URLField(null=True,blank=True)
    text=models.TextField(null=True,blank=True)
    # image=models.ImageField(upload_to='topic_images')
    image_link=models.URLField(null=True,blank=True)

    created_date= models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['-id',]

