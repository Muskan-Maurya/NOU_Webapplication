from django.shortcuts import render,redirect
from nouapp.models import Student , Login
from django.views.decorators.cache import cache_control
from . models import Sturesponse,Question,Answer
from django.contrib import messages
from datetime import date
from adminapp.models import Material
#all values are stored in the cache at the client side

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studenthome(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(request,'studenthome.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
def studentlogout(request):
    try:
        del request.session['rollno']
    except KeyError:
        return redirect('nouapp:login')
    return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def response(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=='POST':
                responsetype=request.POST['responsetype']
                subject=request.POST['subject']
                responsetext=request.POST['responsetext']
                responsedate=date.today()
                rollno=stu.rollno
                name=stu.name
                program=stu.program
                branch=stu.branch
                year=stu.year
                contactno=stu.contactno
                emailaddress=stu.emailaddress
                sr=Sturesponse(rollno=rollno,name=name,program=program,branch=branch,year=year,contactno=contactno,emailaddress=emailaddress,responsetype=responsetype,subject=subject,responsetext=responsetext,responsedate=responsedate)
                sr.save()
                messages.success(request,"success")
            return render(request,'response.html',locals())
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def changepassword(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=='POST':
                oldpassword=request.POST['oldpassword']
                newpassword=request.POST['newpassword']
                confirmpassword=request.POST['confirmpassword']
                if newpassword!=confirmpassword:
                    messages.error(request,'new password and confirm password are not match')
                    return render(request,'changepassword.html',locals())
                try:
                    obj=Login.objects.get(userid=rollno,password=oldpassword)
                    Login.objects.filter(userid=rollno).update(password=newpassword)
                    return redirect('studentapp:studentlogout')
                except:
                    messages.error(request,'old password is not matched')
                    return render(request,'changepassword.html',locals())
            return render(request,'changepassword.html',locals())
    except KeyError:
        return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def postquestion(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=="POST":
                question=request.POST['question']
                postedby=stu.name
                posteddate=date.today()
                Question(question=question,postedby=postedby,posteddate=posteddate).save()
            ques=Question.objects.all()
            return render(request,'postquestion.html',locals())
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def postanswer(request,qid):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            qid=qid
            return render(request,'postanswer.html',locals())
    except KeyError:
        return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def postans(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            qid=request.POST['qid']
            answer=request.POST['answer']
            answerby=stu.name
            posteddate=date.today()
            Answer(answer=answer,answerby=answerby,posteddate=posteddate,qid=qid).save()
            return redirect('studentapp:postquestion')
    except KeyError:
        return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewanswer(request,qid):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            ans=Answer.objects.filter(qid=qid)
            return render(request,'viewanswer.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewprofile(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(request,'viewprofile.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewsmat(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            program=stu.program
            branch=stu.branch
            year=stu.year
            mat=Material.objects.filter(program=program,branch=branch,year=year,materialtype='smat')
            return render(request,'viewsmat.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewassign(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            program=stu.program
            branch=stu.branch
            year=stu.year
            mat=Material.objects.filter(program=program,branch=branch,year=year,materialtype='assign')
            return render(request,'viewassign.html',locals())
    except KeyError:
        return redirect('nouapp:login')