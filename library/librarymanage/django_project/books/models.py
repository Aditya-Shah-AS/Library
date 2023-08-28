from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    isdate=models.DateField()
    enddate=models.DateField()
                            

    def __str__(self):
        return self.title
# Create your models here.
