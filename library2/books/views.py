from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from books.models import Book


# Create your views here.
def home(request):
    context={'name':'anu','age':23}
    return render(request,'home.html',context)

@login_required


def add(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        pa=request.POST['pa']
        l=request.POST['l']
        c=request.FILES['i']
        f=request.FILES['f']

        b=Book.objects.create(title=t,author=a,pages=p,price=pa,language=l,cover=c,pdf=f)
        b.save()
        return view(request)
    return render(request,'add.html')
@login_required
def view(request):
    k=Book.objects.all()
    return render(request,'view.html',{'book':k})

@login_required
def detail(request,i):
    k=Book.objects.get(id=i)
    return render(request,'detail.html',{'book':k})

@login_required
def edit(request,a):
    k=Book.objects.get(id=a)
    if(request.method=="POST"):
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.price=request.POST['pa']
        k.pages=request.POST['p']
        k.language=request.POST['l']
        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.cover=request.FILES['i']
        if(request.FILES.get('f')==None):
            k.save()
        else:
            k.pdf=request.FILES['f']
        k.save()
        return view(request)

    return render(request,'edit.html',{'book':k})
@login_required
def delete(request,p):
    k = Book.objects.get(id=p)
    k.delete()
    return view(request)
from django.db.models import Q
def searchbooks(request):
    k=None


    if(request.method=="POST"):
        query=request.POST['s']
        if query:
            k=Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(language__icontains=query))




    return render(request,'search.html',{'book':k})