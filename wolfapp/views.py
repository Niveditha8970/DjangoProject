from django.shortcuts import render,redirect
from django.http import HttpResponse
from wolfapp.models import Post
import datetime
from wolfapp.forms import EmpForm,ProductModelForm,UserRegister
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def about(request):

    #x='10'
    #print("In views about function")
    return render(request,'about.html')

def classes(request):
    return render(request,'classes.html')

def contact(request):
    return render(request,'contact.html')

def edit(request,rid):

    if request.method=="POST":
        uf=request.POST['fullname']
        ua=request.POST['age']
        ug=request.POST['gender']
        uw=request.POST['weight']
        uc=request.POST['cat']
        us=request.POST['status']
        p=Post.objects.filter(id=rid)
        #print(p)
        p.update(fullname=uf,age=ua,gender=ug,weight=uw,cat=uc,status=us)
        return redirect('/dash')
    
    else:
        p=Post.objects.filter(id=rid)
        #print(p)
        #print(p[0])
        #print(p[0].title)
        content={}
        content['data']=p
        return render(request,'editform.html',content)

def delete(request,rid):


    p=Post.objects.get(id=rid)
    p.delete()
    return redirect('/dash')
 

def abc(request):
    content={'name':'itvedant','rno':10,'per':89.9}
    content['x']= 10
    content['y']= 20
    content['data']= [10,15,20,25,30,35,40,45]
    return render(request,'abc.html',content)

def math(request):
    content={'name':'itvedant'}
    content['x']= 60
    content['y']= 20
    content['z']= 30
    return render(request,'math.html',content)

def reuse(request):
    return render(request, 'base.html')

def index(request):
    return render(request,'index.html')

def dashboard(request):

    if request.user.id:

        user_id=request.user.id
        p=Post.objects.filter(uid=user_id) # fetch all rows or objects and storied in p
        content={}
        content['data']=p
        return render(request,'dashboard.html',content)
 
    else:
        return redirect('/login')

def create_post(request):
    #print(request.method)
    if request.user.id:

        user_id=request.user.id
        #print(user_id)
        if request.method=="POST":
            f=request.POST['fullname']
            a=request.POST['age']
            g=request.POST['gender']
            w=request.POST['weight']
            bcat=request.POST['cat']
            stat=request.POST['status']

            content={}
            if f=='':
                content['msgf']="Fullname cannot be blabk"
            elif a=='':
                content['msga']="Age cannot be blank"
            elif g=='':
                content['msgg']="Gender cannot be blank"
            elif w=='':
                content['msgw']="Weight cannot be blank"
            elif bcat not in ('1','2','3'):
                content['msgcat']="Please select valid Input for select category"
            elif stat not in ('0','1'):
                content['msgstat']="Please senter valid input for status"
            else:
                p=Post.objects.create(fullname=f,age=a,gender=g,weight=w,cat=bcat,status=stat,created_on=datetime.datetime.now(),uid=user_id)
                p.save()
                return redirect('/dash')

            return render(request,'create_post.html',content)
        
        else:
            return render(request,'create_post.html')

    else:
        return redirect('/login')


    
def catfilter(request,value): #1,2,3
    p=Post.objects.filter(cat=value) #select * from wolf_post where cat=1/2/3
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)

def actfilter(request,value): #1,2,3
    p=Post.objects.filter(status=value) #select * from wolf_post where cat=1/2/3
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)

def djangoform(request):

    if request.method=="POST":
        n=request.POST['name']
        eid=request.POST['empid']
        sal=request.POST['sal']
        print("Employee Name:",n)
        print("Employee ID:",eid)
        print("Salary:",sal)

    else:
    
        fm=EmpForm()
        #print(fm)
        content={}
        content['formdata']=fm
        return render(request,'djangoform.html',content)

        #return HttpResponse("Form object printed in Terminal")

def djangomodelform(request):
    if request.method=="POST":
        Pass

    else:

        fm=ProductModelForm()
        #print(fm)
        content={}
        content['mformdata']=fm
        return render(request,'addproduct.html',content)
        #return HttpResponse("Model form object printed in Terminal")


def user_register(request):

    if request.method=="POST":
        regfmdata=UserRegister(request.POST)
        #print(regfmdata)
        #print(regfmdata.is_valid()) #it will be either true or false
        message={}
        if regfmdata.is_valid():
            regfmdata.save()
            message['msg']="Congratulation,Registration Done Successfully"
            message['x']=1
            return render(request,'register_success.html',message)

        else:
            message['msg']="Faild to Register User.Please Try Again"
            message['x']=1
            return render(request,'register_success.html',message)
    
    else:
        #regfm=UserCreationForm()
        regfm=UserRegister()
        #print(regfm)
        content={}
        content['regfmdata']=regfm
        return render(request,'register.html',content)

        #return HttpResponse("Form object printed on triminal")


def user_login(request):

    fmlog=AuthenticationForm()
    content={}
    content['logfmdata']=fmlog
    if request.method=="POST":
        logfmdata=AuthenticationForm(request=request,data=request.POST)
        #print(logfmdata)
        if logfmdata.is_valid():
             uname=logfmdata.cleaned_data['username']
             upass=logfmdata.cleaned_data['password']
             #print("Username:",uname)
             #print("Password:",upass)
             r=authenticate(username=uname,password=upass)
             #print("value returned by Authenticate"r)
             if r is not None:
                login(request,r)#start session and sote id of lo9gged in user
                return redirect('/dash')
        else:
            
            content['msg']="Invalid username and password!!!"
            return render(request,'login.html',content)
           

    else:
        fmlog=AuthenticationForm()
        content={}
        content['logfmdata']=fmlog
        return render(request,'login.html',content)


def user_logout(request):

    logout(request)#it destroy session data
    return redirect('/login')



def setcookies(request):
    res=render(request,'setcookie.html')#response object
    #print(res)
    res.set_cookie('name','niveditha')
    res.set_cookie('rno',35)
    res.set_cookie('per',89.9)
    return res 


def getcookies(request):
    name=request.COOKIES['name']
    r=request.COOKIES['rno']
    p=request.COOKIES['per']
    content={'n':name,'roll':r,'per':p}
    return render(request,'getcookie.html',content)


def setsession(request):
    request.session['uname']="firstuser"

    return render(request,'setsession.html')

def getsession(request):
    d=request.session['uname']#accessing session data
    content={}
    content['n']=d
    return render(request,'getsession.html',content)


    



