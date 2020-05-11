from Home.forms import ContactForm
from django.shortcuts import render


def index(request):
    """ Render home page """
    return render(request, 'Home/index.html')


def about(request):
    """ Render about page """
    return render(request, 'home/about.html')


def services(request):
    """ Render services page """
    return render(request, 'Home/services.html')


def contact(request):
    """ Render contact page """

    form = ContactForm(request.POST or None)

    if form.is_valid():
        content = form.cleaned_data['content']
        author = form.cleaned_data['author']

        # Send the  mail here

    return render(request, 'Home/contact.html', locals())
