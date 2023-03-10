from django.db import models

# Create your models here.


class Doctor(models.Model):
    Name = models.CharField(max_length=100)
    Degree = models.CharField(max_length=100)
    Contact = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='docimage/')
    Category = models.CharField(max_length=100,choices=(('lungsSpecialist', "lungsSpecialist"),
                  ('eyespecialist', 'eyespecialist'),
                  ('heartspecialist', 'heartspecialist'),
                  ('legspecialist', 'legspecialist'),
                  ),default='eyespecialist')


class User(models.Model):
    Name = models.CharField(max_length=100)
    Contact = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
