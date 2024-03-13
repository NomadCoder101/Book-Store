from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from django.shortcuts import reverse

from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author=models.CharField(null=True,max_length=100)
    is_bestselling=models.BooleanField(default=False)
    slug= models.SlugField(default="",null=False,blank=True,db_index=True)
    
    def get_absolute_url(self):
        return reverse("detail_page", args=[self.slug])
    
    # def save(self,*args,**kwargs):

    #     self.slug =slugify(self.title)   ==> replaced after adding the admin prepopulate_field

    #     super().save(*args,**kwargs)
    
    
    def __str__(self):
        
        return f"{self.title} ({self.rating})"