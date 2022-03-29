from django.db import models

# Create your models here.

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=120)
    subject=models.TextField()
    time=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
       return f"{self.name}-{self.email}"
   
    