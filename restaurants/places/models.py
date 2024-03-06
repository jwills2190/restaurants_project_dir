from django.db import models
from django.urls import reverse

# Create your models here.
class Cuisine(models.Model):
    cuisine_name = models.CharField(max_length=25)
    cuisine_desc = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.cuisine_name}"
    
class Review(models.Model):
    comment = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return f"{self.comment}"

class Restaurant(models.Model):
    name = models.CharField(max_length=50, blank=False)
    cuisine = models.ManyToManyField(Cuisine, blank=True, related_name='cuisines')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.DecimalField(blank = True,max_digits = 2,decimal_places = 1)
    price_point = models.IntegerField(blank = True)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, null=True,blank=True)
    address3 = models.CharField(max_length=50, null=True, blank=True)
    address_city = models.CharField(max_length=50, blank=True)
    address_state = models.CharField(max_length=50, blank=True)
    address_zipcode = models.CharField(max_length=9, blank=True)
    tel_number = models.CharField(max_length=25, blank=True)
    email_addr = models.CharField(max_length=50, blank=True)
    smoking_allowed = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True, upload_to = 'restaurants')
    image_url = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.name}, {self.cuisine}"
    
    def get_absolute_url(self):
        return reverse("restaurant-detail", kwargs={"pk": self.pk})
    