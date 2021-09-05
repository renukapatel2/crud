from django.shortcuts import render,redirect
from .models import *
# Create your views here.



def Cruds(request):
    rn = User.objects.all()
    return render(request,"apps/cruds.html",{'vs':rn})

def register(request):
    return render(request,"apps/Register.html")

def Edituser(request,pk):
    sel = User.objects.get(id=pk)
    return render(request,"apps/edituser.html",{'sel':sel})

def adduser(request):
    if request.method == 'POST':
        fn= request.POST['fname']
        ln= request.POST['lname']
        em= request.POST['email'] 
        psw= request.POST['passw']
        im = request.FILES['image']

        add = User.objects.create(
            fname= fn,
            lname= ln,
            email= em,
            pas= psw,
            img= im
        )
        return redirect('cruds')
    else:
        pass
def UserDelete(request,pk):
    pro = User.objects.get(id=pk)
    pro.delete()
    return redirect("cruds")
    
def Update(request,pk):
    pro =  User.objects.get(id=pk)
    pro.fname =  request.POST['fname'] if request.POST['fname'] else pro.fname
    pro.lname = request.POST['lname'] if request.POST['lname'] else pro.lname
    pro.email = request.POST['email'] if  request.POST['email']  else pro.email
    pro.pas = request.POST['passw'] if request.POST['passw'] else pro.pas
    try:
        pro.img = request.FILES['img'] if request.FILES['img'] else pro.img
    except:
        pass
    pro.save()
    return redirect("cruds")
    

    
