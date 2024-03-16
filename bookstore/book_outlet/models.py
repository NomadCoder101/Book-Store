from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from django.shortcuts import reverse

from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural="Countries"

class Address(models.Model):
    street=models.CharField(max_length=200)
    postal_code=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.street},{self.posta_code},{self.city}"
    
    class Meta:
        verbose_name_plural="Address Entries"
  

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True)
   
    
        
    def __str__(self):
        
        return f"{self.first_name} "
    


    

class Book(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author=models.ForeignKey(Author, on_delete=models.CASCADE,null=True,related_name='books')
    is_bestselling=models.BooleanField(default=False)
    slug= models.SlugField(default="",null=False,blank=True,db_index=True)
    published_country=models.ManyToManyField(Country)
    
    
    
    def get_absolute_url(self):
        return reverse("detail_page", args=[self.slug])
    
    # def save(self,*args,**kwargs):

    #     self.slug =slugify(self.title)   ==> replaced after adding the admin prepopulate_field

    #     super().save(*args,**kwargs)
    
    
    def __str__(self):
        
        return f"{self.title} ({self.rating})"
