from django.db import models

# Create your models here.
class Employee(models.Model):

    name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    image=models.ImageField(upload_to="images")


    def __str__(self):
        return self.name
