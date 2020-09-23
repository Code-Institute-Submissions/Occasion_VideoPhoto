from django.shortcuts import render

# Create your views here.


def contact(request):
    """ A Views to return the index page """
    return render(request, "contact/contact.html")
