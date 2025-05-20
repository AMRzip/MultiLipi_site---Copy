from django.db import models

# Create your models here.
class Request_a_Demo(models.Model):
    site_name = models.CharField(max_length=250)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_no = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.email