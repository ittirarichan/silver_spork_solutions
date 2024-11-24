from django.db import models

# Create your models here.
class Course(models.Model):
    c_id=models.TextField()
    c_name=models.TextField()
    dis=models.TextField()
    duration=models.IntegerField()
    Course_fees=models.IntegerField()
    offer_fees=models.IntegerField()
    img=models.FileField()

class Contact(models.Model):
    name=models.TextField()
    email=models.EmailField()
    message=models.TextField()