from django.shortcuts import render
from .models import Topics, Question
import json
import sys

# Create your views here.


def home(request):
    topics_objects = Topics.objects.all()
    context = {'topics': topics_objects}
    return render(request, 'py_pro_app/home.html', context)


def qa_page(request, pk):
    topics_objects = Topics.objects.all()
    data = Question.objects.filter(topic__title__contains=pk)
    # print(data)
    context = {'data': data, 'topics': topics_objects}
    return render(request, 'py_pro_app/qa.html', context)

def runcode_(request):
    if request.method =='POST':
        code = request.POST['codearea']
        try:
            original = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code)
            sys.stdout.close()
            sys.stdout = original
            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout = original
            output = e
        return render(request, 'pycompiler/py-compiler.html', {'code':code, 'output':output})

    return render(request, 'pycompiler/py-compiler.html')



def runcode(request, pk):

    data = Question.objects.get(pk=pk)
    return render(request, 'pycompiler/py-compiler.html', {'code': data.code})