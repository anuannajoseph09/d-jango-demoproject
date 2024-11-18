from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from emp.models import Employee


# Create your views here.
def home(request):
    context={'name':'anu','age':23}
    return render(request,'home.html',context)





def view(request):
    return render(request, 'view.html')


#
def add(request):
    if(request.method=="POST"):

        n=request.POST['n']
        a=request.POST['a']
        ad=request.POST['ad']
        e=request.POST['e']
        im=request.FILES['i']

        b=Employee.objects.create(name=n,age=a,address=ad,email=e,image=im)
        b.save()
        return view(request)
    return render(request,'add.html')

def view(request):
    k=Employee.objects.all()
    return render(request,'view.html',{'emp':k})

def detail(request,i):
    k=Employee.objects.get(id=i)
    return render(request,'detail.html',{'emp':k})

def edit(request,a):
    k=Employee.objects.get(id=a)
    if(request.method=="POST"):
        k.name=request.POST['n']
        k.age=request.POST['a']
        k.address=request.POST['ad']
        k.email=request.POST['e']
        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.image=request.FILES['i']

        k.save()
        return view(request)

    return render(request,'edit.html',{'emp':k})

def delete(request,p):
    k = Employee.objects.get(id=p)
    k.delete()
    return view(request)


# Create your views here.
