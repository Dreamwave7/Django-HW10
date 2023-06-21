from django.forms import ModelForm, CharField, TextInput, ModelMultipleChoiceField, SelectMultiple,Select,ModelChoiceField
from pymongo import MongoClient
from .models import *
def get_mongo():
    client = MongoClient("mongodb+srv://guest:guest@dreamwave.dhurwpi.mongodb.net/?retryWrites=true&w=majority")
    db = client.module8
    return db

db = get_mongo()

class QuoteForm(ModelForm):
    quote = CharField(required=True, widget=TextInput())
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by('name'), required = True, widget=SelectMultiple()) 
    author = ModelChoiceField(queryset=Author.objects.all().order_by("fullname"), widget=Select(), required= True)

    class Meta:
        model = Quote
        fields = ["quote","author","tags"]


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50,required=True,widget=TextInput())
    born = CharField(max_length=300, required= True, widget=TextInput())
    bio = CharField(required=True, widget= TextInput())

    class Meta:
        model = Author
        fields =["fullname","born","bio"]


class TagForm(ModelForm):
    name = CharField(min_length=2, max_length=30, required=True,widget=TextInput())

    class Meta:
        model = Tag
        fields = ["name"]

        


















