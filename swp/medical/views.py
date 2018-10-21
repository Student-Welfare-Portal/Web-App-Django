from django.shortcuts import render

# Create your views here.
def medical_dashboard(request):
    return render(request,'medical/medical_dashboard.html')
def medical_message(request):
    return render(request,'medical/medical_message.html')
def medical_leave(request):
    return render(request,'medical/medical_leave.html')
def sendMessage(request):
    print(request.POST['subject'])
    return render(request,'medical/medical_message.html')
