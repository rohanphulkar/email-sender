from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings

# main page views 
def index(req):
    # sending email if request method is POST
    if req.method == 'POST':
        email = req.POST.get('email')
        subject = req.POST.get('subject')
        message = req.POST.get('message')
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
        return redirect("success_page")
    return render(req,"index.html")

def success(req):
    return render(req,"success.html")