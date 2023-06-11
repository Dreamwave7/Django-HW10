from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=300, null=False, unique=True)

    def __str__(self) -> str:
        return self.name
    

class Note(models.Model):
    name = models.CharField(max_length=250, null=False)
    description = models.CharField(max_length=250,null=False)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.name