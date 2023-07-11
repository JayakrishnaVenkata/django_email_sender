
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
# Create your views here.

def home(request):
    email=request.POST.get('email')
    subject=request.POST.get('subject')
    # subject = "pavram"
    # message = "Bava ma chelli ela undi"
    message = request.POST.get('message')
    from_me = settings.EMAIL_HOST_USER
    to_you  = []
    to_you.append(email)
    print(to_you)
    send_mail(subject,message,from_me,to_you)
    to_you = []
    return render(request,'home.html')
