from django.shortcuts import render
from .models import Topics

# Create your views here.


def home(request):
    topics_objects = Topics.objects.all()
    context = {'topics': topics_objects}
    return render(request, 'py_pro_app/navbar.html', context)


def qa_page(request, pk):
    topic = Topics.objects.get(pk=pk)
    return render(request, 'py_pro_app/qa.html')