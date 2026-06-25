from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.ImageField(upload_to='covers/')
    description = models.TextField()
    stock = models.IntegerField()
    def __str__(self):
        return self.title
