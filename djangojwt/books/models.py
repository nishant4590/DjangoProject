from django.db import models

class books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
    
class students(models.Model):
    name = models.CharField(max_length=255)
    std = models.CharField(max_length=255)
    age = models.CharField(max_length=15)

    def __str__(self):
        return self.name
