from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import MedicalLeaveForm
from .models import *
from django.contrib.auth.decorators import login_required
from accounts.models import Student
import datetime
# Create your views here.
@login_required
def medical_dashboard(request):
    return render(request,'medical/medical_dashboard.html')
@login_required
def medical_message(request):
    return render(request,'medical/medical_message.html')
@login_required
def medical_leave(request):
    form=MedicalLeaveForm()
    return render(request,'medical/medical_leave.html',{'form':form})
@login_required
def sendMessage(request):
    subject=request.POST['subject']
    to_email=request.POST['to']
    body=request.POST['body']
    message=render_to_string('medical/message.html',{'from':request.user.username,'body':body})
    email=EmailMessage(subject,message,to=[to_email])
    email.send()
    return render(request,'medical/success.html')
def getDate(s):
    s=s.split('-')
    year=int(s[0])
    month=int(s[1])
    day=int(s[2])
    return datetime.date(year,month,day)
@login_required
def applyLeave(request):
    leave_from=request.POST['leave_from']
    leave_to=request.POST['leave_to']
    hometown=request.POST['hometown']
    reason=request.POST['reason']
    student=Student.objects.get(user=request.user)
    leave_from=getDate(leave_from)
    leave_to=getDate(leave_to)
    print(student,leave_from,leave_to,hometown,reason)

    leave=MedicalLeave(leave_from=leave_from,leave_to=leave_to,hometown=hometown,reason=reason,student=student)
    leave.save()
    return render(request,'medical/success.html')
