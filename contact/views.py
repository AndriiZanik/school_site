from django.shortcuts import render,get_object_or_404,redirect
from contact.models import Responses
from contact.forms import ResponseForm


def contacts_page(request):
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.save()
        #return redirect()
    else:
        form = ResponseForm()
    context = {'Title': 'Контакти','form': form}
    return render(request=request, template_name='Contacts_page.html', context=context)


def add_response(request):
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            Responses.objects.create(**form.cleaned_data)
            #return redirect()
    else:
        form = ResponseForm()
    return render(request, 'add_response.html', {'form': form})
