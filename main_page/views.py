from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    news = News.objects.all()
    context = {'Title':'Main Page',
               'news':news}
    return render(request=request,template_name='main_page/news_on_main_page.html',context=context)
