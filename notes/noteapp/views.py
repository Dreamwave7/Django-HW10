from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from pprint import *


def index(request):
    notes = Note.objects.all()
    return render(request, "noteapp/index.html",{"notes":notes})

def tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="noteapp:index")
        else:
            return render(request, "noteapp/index.html",{"form":form})
        
    return render(request, "noteapp/tag.html", {"form":TagForm()})



def note(request):
    tags = Tag.objects.all()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()
        
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist("tags"))
            for tag in choice_tags:
                new_note.tags.add(tag)
            return redirect(to="noteapp:index")
        else:
            return render(request, "noteapp/note.html",{"tags":tags,"form":form})
        
    return render(request, 'noteapp/note.html', {"tags": tags, 'form': NoteForm()})

def detail(request, note_id):
    note = get_object_or_404(Note, pk = note_id)
    return render(request,"noteapp/detail.html",{"note":note})


def set_done(request, note_id):
    Note.objects.filter(pk=note_id).update(done=True)
    return redirect(to='noteapp:index')


def delete_note(request, note_id):
    Note.objects.get(pk=note_id).delete()
    return redirect(to='noteapp:index')











































