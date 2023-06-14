from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=300, null=False, unique=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user","name"], name="tag of username")
            ]

    def __str__(self) -> str:
        return self.name
    

class Note(models.Model):
    name = models.CharField(max_length=250, null=False)
    description = models.CharField(max_length=250,null=False)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.name