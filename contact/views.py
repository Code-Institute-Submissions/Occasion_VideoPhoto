from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def contact(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['msg']
        email_subject = "You have a new email from Occasion Video&Photo"
        message_body = "Name: " + name + " Email: " + email + "Message: " + msg

        send_mail(
            email_subject,
            message_body,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return redirect("contact")

    return render(request, "contact/contact.html")   
