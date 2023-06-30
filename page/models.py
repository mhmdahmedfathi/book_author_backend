from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=255,null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey('book.Book', related_name='pages' ,on_delete=models.CASCADE)
    author = models.ForeignKey('author.Author', related_name='pages', on_delete=models.CASCADE)