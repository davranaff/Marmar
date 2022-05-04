from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=40)
    image1 = models.ImageField(upload_to='projects/', null=True)
    image2 = models.ImageField(upload_to='projects/', null=True)
    image3 = models.ImageField(upload_to='projects/', null=True)
    text = models.TextField()
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Staff(models.Model):
    name = models.CharField(max_length=40)
    position = models.TextField()
    image = models.ImageField(upload_to='staffs/')

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Contact(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=30)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'