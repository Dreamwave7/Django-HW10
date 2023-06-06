from django.contrib import admin

# Register your models here.
from .models import Tag, Note

admin.site.register(Tag)
admin.site.register(Note)