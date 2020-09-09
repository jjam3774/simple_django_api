from django.db import models

# Create your models here.
class Book(models.Model):
    author      = models.CharField(max_length=100)
    title       = models.CharField(max_length=100)
    isbn        = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return "%s | %s | isbn: %s" % (self.author, self.title, self.isbn)
