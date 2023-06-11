from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . models import regtable

# Create your views here.

def index(request):
    return render(request,'index.html')
def userlogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        obj=regtable.objects.filter(email=email,password=password)
        if obj:
            request.session['eml']=email
            request.session['pass']=password
            return render(request,'inc/userhome.html')
        else:
            msg="invalid email and password"
            request.session['eml']=''
            request.session['pass']=''
            return render(request,'inc/userlogin.html',{"error":msg})
    else:
        return render(request,'inc/userlogin.html')
def userreg(request):

    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        address=request.POST.get('address')
        State=request.POST.get('State')
        Zip=request.POST.get('Zip')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        code=request.POST.get('code')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        obj=regtable.objects.create(fname=fname,lname=lname,email=email,address=address,State=State,pincode=Zip,DOB=dob,gender=gender,code=code,phoneno=phone,password=password,confirmpassword=confirmpassword)
        obj.save()
        if obj:
            return render(request,"inc/userlogin.html")
        else:
            return render(request,'inc/userreg.html')
    else:
            
        return render(request,'inc/userreg.html')
    

def userhome(request):
    return render(request,'inc/userhome.html')
def header(request):
    return render(request,'component/header.html')
def footer(request):
    return render(request,'component/footer.html')
def sports_items(request):
    return render(request,'inc/sports_items.html') 
def turf_view(request):
    return render(request,'inc/turf_view.html') 
def event_view(request):
    return render(request,'inc/event_view.html') 
def academy_view(request):
    return render(request,'inc/academy_view.html')       