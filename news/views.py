from django.shortcuts import render
from .models import News, Category
from django.http import HttpResponse

def index(request):

    news=News.objects.all()
    context={
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context)



def test(request):
    return HttpResponse('<h1>Тестовая страница<h1>')