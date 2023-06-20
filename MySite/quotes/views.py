from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from pymongo import MongoClient

def get_mongo():
    client = MongoClient("mongodb+srv://guest:guest@dreamwave.dhurwpi.mongodb.net/?retryWrites=true&w=majority")
    db = client.module8
    return db


def index(request):
    db = get_mongo()
    quotes = db.quotes.find()
    name = request.user
    return render(request,"quotes/index.html", context={"quotes":quotes,"name":name})

def author_bio(request, author_name):
    print(author_name)
    db = get_mongo()
    author = db.authors.find_one({"fullname":author_name})
    print(author)
    return render(request,"quotes/author.html", context={"author":author})



















