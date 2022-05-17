from django.views.generic import ListView, DeleteView

from info.models import Teacher


class InfoMain(ListView):
    model = Teacher
    template_name = 'info_main.html'

class InfoTeachers(ListView):
    model = Teacher
    template_name = 'info_about_teachers.html'
    # context_object_name = 'teachers'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InfoTeachers, self).get_context_data()
        context['title'] = 'Info page'
        return context




# def get_queryset(self):
#     return News.objects.filter(is_published=True)




#
# class ViewAuthor(DeleteView):
#     model = Author
#     template_name = 'view_author.html'
