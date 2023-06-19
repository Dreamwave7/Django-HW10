from django.db import models

# Create your models here.

class Author(models.Model):
    fullname = models.CharField(max_length=100)
    born = models.CharField(max_length=200)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.fullname
    
class Tag(models.Model):
    name = models.CharField(null=False,unique=True)
    def __str__(self) -> str:
        return self.name

class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.quote
    

