from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    pages = models.IntegerField()
    author = models.ForeignKey('authors.Author', related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title