from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import MedicalLeaveForm
# Create your views here.
def medical_dashboard(request):
    return render(request,'medical/medical_dashboard.html')
def medical_message(request):
    return render(request,'medical/medical_message.html')
def medical_leave(request):
    return render(request,'medical/medical_leave.html')
def sendMessage(request):
    subject=request.POST['subject']
    to_email=request.POST['to']
    body=request.POST['body']
    message=render_to_string('medical/message.html',{'body':body})
    email=EmailMessage(subject,message,to=[to_email])
    email.send()
    return render(request,'medical/medical_message.html')
