import os
import django

from pymongo import MongoClient


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MySite.settings')
django.setup()


from quotes.models import Quote, Tag, Author

client = MongoClient("mongodb+srv://guest:guest@dreamwave.dhurwpi.mongodb.net/?retryWrites=true&w=majority")


db = client.module8
print("connected to base")

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname = author["fullname"],
        born = author["born_date"] ,
        bio = author["description"]
        )
    
    
quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote["tags"]:
        t, *_ =Tag.objects.get_or_create(name=tag)
        tags.append(t)
    
    exist_quote = bool(len(Quote.objects.filter(quote=quote["quote"])))

    if not exist_quote:
        try:
            author = db.authors.find_one({"fullname": quote["author"]})
            a = Author.objects.get(fullname=author["fullname"])
            q = Quote.objects.create(
                quote = quote["quote"],
                author = a
                )
            for tag in tags:
                q.tags.add(tag)
        except:
            print(quote["author"])


    
    

     
