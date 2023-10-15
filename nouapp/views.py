from django.shortcuts import render,redirect,reverse
from . models import Enquiry,Student,Login
from django.contrib import messages
from datetime import date
from adminapp.models import News
from . smssender import sendsms
from . forms import MyForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    nw=News.objects.all()
    return render(request,'index.html',locals())
def aboutus(request):
    nw=News.objects.all()
    return render(request,'aboutus.html',locals())
def registration(request):
    form=MyForm()
    if request.method=="POST":
        form=MyForm(request.POST)
        if form.is_valid():
            rollno=request.POST['rollno']
            name=request.POST['name']
            fname=request.POST['fname']
            mname=request.POST['mname']
            gender=request.POST['gender']
            dob=request.POST['dob']
            address=request.POST['address']
            program=request.POST['program']
            branch=request.POST['branch']
            year=request.POST['year']
            contactno=request.POST['contactno']
            emailaddress=request.POST['emailaddress']
            password=request.POST['password']
            regdate=date.today()
            usertype='student'
            status='false'
            stu=Student(rollno=rollno,name=name,fname=fname,mname=mname,gender=gender,dob=dob,address=address,program=program,branch=branch,year=year,contactno=contactno,emailaddress=emailaddress,regdate=regdate)
            log=Login(userid=rollno, password=password ,usertype=usertype,status=status)
            stu.save()
            log.save()
            subject='Important mail from Nalanda  Open University'
            mssg=f"Hello,{name} your registration is done and your roll number is {rollno},password is {password}"
            email_from=settings.EMAIL_HOST_USER
            send_mail(subject,mssg,email_from,[emailaddress])
            messages.success(request,'Student is register')
        else:
            messages.success(request,'Invalid Captcha Code')
    nw=News.objects.all()
    return render(request,'registration.html',locals())
def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        try:
            obj=Login.objects.get(userid=userid,password=password)
            if obj.usertype=='student':
                request.session['rollno'] = userid
                return redirect(reverse('studentapp:studenthome'))
            elif obj.usertype=='admin':
                request.session['adminid'] = userid
                return redirect(reverse('adminapp:viewstudent'))
        except:
            messages.error(request,'Invalid user')
    nw=News.objects.all()
    return render(request,'login.html',locals())
def contactus(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        address=request.POST['address']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        enquirytext=request.POST['enquirytext']
        enquirydate=date.today()
        #ORM(object relationship mapping)(model name=variable in view)
        enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
        enq.save()
        sendsms(contactno)
        messages.success(request,'Your Enquiry is Submitted')
    nw=News.objects.all()
    return render(request,'contactus.html',locals())