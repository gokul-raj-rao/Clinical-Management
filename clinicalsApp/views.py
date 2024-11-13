from django.shortcuts import render
from clinicalsApp.models import Patient, ClinicalData
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from clinicalsApp.forms import ClinicalDataForm
from clinicalsApp.models import MyModel
from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

#select Date
from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ STEP 4 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create your views here.
        


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")  
        email = request.POST.get("email")  
        phone = request.POST.get("phone")  
        date = request.POST.get("date")  
        dname = request.POST.get("dname")
        message = request.POST.get("message") 
        time=request.POST.get("time") 

        MyModel.objects.create(name=name,email=email,phone=phone,date=date,dname=dname,message=message,time=time)
        with get_connection(  
           host=settings.EMAIL_HOST, 
     port=settings.EMAIL_PORT,  
     username=settings.EMAIL_HOST_USER, 
     password=settings.EMAIL_HOST_PASSWORD, 
     use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           subject = "Appoinment Success"  
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = [email, ]  
           message = f"Your Appointment request is successfully Registered. \n\nYour Name: mr/ms: {name}\nDate of appointment is {date} \nYour Apointment time is {time}\nDoctor name is {dname} \nYour mobile number is {phone}"
           EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
    return render(request, "Medilab/index.html")


class PatientListView(ListView):
    model= Patient

class PatientCreateView(CreateView):
    model= Patient
    success_url= reverse_lazy('index')
    fields= ('firstName','lastName','age')

class PatientUpdateView(UpdateView):
    model= Patient
    success_url= reverse_lazy('index')
    fields= ('firstName','lastName','age')

class PatientDeleteView(DeleteView):
    model= Patient
    success_url= reverse_lazy('index')


def addData(request, **kwargs):
    form= ClinicalDataForm
    patient= Patient.objects.get(id=kwargs['pk'])
    if request.method=="POST":
        form=ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    return render(request, 'clinicalsApp/clinicaldata_form.html',{'form':form,'patient':patient})


def analyze(request, **kwargs):
    data= ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responsedata=[]
    for eachEntry in data:
        if eachEntry.componentName=='hw':
            heightweight= eachEntry.componentValue.split('/')
            if len(heightweight) > 1:
                feetTometers= float(heightweight[0]) * 0.4536
                BMI= (float(heightweight[1]))/(feetTometers*feetTometers)
                bmiEntry= ClinicalData()
                bmiEntry.componentName='BMI'
                bmiEntry.componentValue=BMI
                responsedata.append(bmiEntry)
        responsedata.append(eachEntry)
    return render(request, 'clinicalsApp/generateReport.html', {'data':responsedata})


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request, "Medilab/login.html")



def LogoutPage(request):
    logout(request)
    return redirect('login')



def select_date(request):
    if request.method == 'POST':
        selected_date = request.POST['date']
        date_object = datetime.strptime(selected_date, '%Y-%m-%d').date()
        records = MyModel.objects.filter(date=date_object)
        return render(request, 'clinicalsApp/view_patients.html', {'records': records, 'selected_date': selected_date})
    return render(request, 'clinicalsApp/select_date.html')


def pa(request):    
    records = MyModel.objects.all()
    return render(request, 'clinicalsApp/patient.html',{"records": records})

def delete_appointment(request, post_id):
    values = get_object_or_404(MyModel, pk=post_id)
    email=values.email
    print("^^^^^^^^^^^^^^^", email)
    with get_connection(  
           host=settings.EMAIL_HOST, 
     port=settings.EMAIL_PORT,  
     username=settings.EMAIL_HOST_USER, 
     password=settings.EMAIL_HOST_PASSWORD, 
     use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           subject = "Appoinment Failed"  
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = [email, ]  
           message = f"Sorry, Your Appointment request is Declined. \nUnfortunately, There is no availability which you have requested. \nCall +91782387329 for assistance"
           EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
    
    values.delete()
    
    return redirect('all')
        

    