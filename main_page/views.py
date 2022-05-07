from django.shortcuts import render
from .models import News

def index(request):
    news = News.objects.all()
    context = {'Title':'Main Page',
               'news':news}
    return render(request=request, template_name='main_page_news.html', context=context)

def contacts_page(request):
    context = {'Title':'Контакти'}
    return render(request=request, template_name='Contacts_page.html', context=context)


