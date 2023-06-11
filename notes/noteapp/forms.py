from django.forms import ModelForm, CharField, TextInput
from .models import Tag, Note

class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=250,required=True,widget=TextInput())

    class Meta:
        model = Tag
        fields = ["name"]


class NoteForm(ModelForm):
    name = CharField(min_length=3,max_length=40,required=True,widget=TextInput())
    description = CharField(min_length=5,max_length=400,required=True,widget=TextInput())

    class Meta:
        model = Note
        fields = ["name","description"]
        exclude = ["tags"]