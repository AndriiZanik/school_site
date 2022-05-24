from django.views.generic import ListView,DeleteView,View,TemplateView
from .models import News,Author
from django.db.models import Q

class MainNews(ListView):
    model = News
    template_name = 'main_page_news.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainNews, self).get_context_data()
        context['title'] = 'Main page'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)

class AboutUs(TemplateView):
    template_name = 'about_us.html'

class ViewNews(DeleteView):
    model = News
    template_name = 'view_news.html'

class ViewAuthor(DeleteView):
    model = Author
    template_name = 'view_author.html'

class SearchResultsView(ListView):
    model = News
    template_name = 'search_results.html'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = News.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return object_list


# def get_news(request, news_id):
#     news = News.objects.filter(news_id == id)
#     nov = News.objects.get(id == news_id)
#     return render(request,'view_news.html',{'news':news,'nov':nov})
#
#
# def view_news(request,news_id):
#     news_item = News.objects.get(pk = news_id)
#     return render('view_news.html',{'news_item':news_item})

#
# def index(request):
#     news = News.objects.all()
#     context = {'Title':'Main Page',
#                'news':news}
#     return render(request=request, template_name='main_page_news.html', context=context)
#
#
#
#
