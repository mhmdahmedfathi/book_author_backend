from django.db import models

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('author.Author', related_name='books', on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    cover = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.title