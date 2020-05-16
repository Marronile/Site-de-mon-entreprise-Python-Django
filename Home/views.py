from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail


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
    author = request.POST.get('author', '')
    content = request.POST.get('content', '')
    message = ""
    if author and content:
        try:
            send_mail("Message from Marronile.com", content,
                      author, ['dah.kenangnon@gmail.com'])
            message = "Email envoyé avec succès!"
        except BadHeaderError:
            message = "Erreur inconnue"
    return render(request, 'Home/contact.html', locals())
