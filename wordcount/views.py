from django.shortcuts import render
from .models import Blog
from .models import File
# Create your views here.

def base(request):
    blogs = Blog.objects
    return render(request,'base.html', {'blogs':blogs})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] +=1
        else:
            word_dictionary[word] =1

    return render(request, 'result.html', {'full':text , 'total':len(words), 
    'dictionary':word_dictionary.items()})

def new(request):
    return render(request,'new.html')

def savefiles(request):
    files = File.objects
    return render(request, 'savefiles.html',{'files':files})
