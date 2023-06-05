from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

def index(request):
    latest_question = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("dell/index.html")
    context = {
        "latest_question_list": latest_question
        }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "dell/detail.html", {"question": question})
def results(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    return  render(request,"dell/results.html",{"question":question})

def vote(request, question_id):
    question = get_object_or_404(Question,pk= question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExists):
        return render(request, "dell/details.html",{
            "question":question,
            "error_message": "You didnt select a choice."
            })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("dell:results", args=(question.id,)))