from django.shortcuts import render
from .models import Topics, Question
import json

# Create your views here.


def home(request):
    topics_objects = Topics.objects.all()
    context = {'topics': topics_objects}
    return render(request, 'py_pro_app/home.html', context)


def qa_page(request, pk):
    topics_objects = Topics.objects.all()
    data = Question.objects.filter(pk=pk)
    print(data)


    context = {'data': data, 'topics': topics_objects}

    return render(request, 'py_pro_app/qa.html', context)