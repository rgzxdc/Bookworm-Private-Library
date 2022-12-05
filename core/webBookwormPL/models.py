from django.db import models

class BookList(models.Model):
    title = models.CharField(max_length=100,null=False)
    author_name = models.EmailField(max_length=100,null=False)
    genre = models.CharField(max_length=30,null=True)
    added_date = models.DateField
    isbn = models.IntegerField(null=True)
