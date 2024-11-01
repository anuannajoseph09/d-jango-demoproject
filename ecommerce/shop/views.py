from django.shortcuts import render
from shop.models import Category,Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from shop.models import Users
from cart.models import Order_details
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.



def allcategories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'category.html',context)



def allproducts(request,p):
    c=Category.objects.get(id=p)
    p=Product.objects.filter(category=c)
    context={'cat':c,'product':p}
    return render(request,'product.html',context)


def detail(request,i):
    k=Product.objects.get(id=i)
    return render(request,'detail.html',{'product':k})




# Create your views here.
def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']

        if(p==cp):
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            u.save()
        else:
            return HttpResponse("password are not same")
        return redirect('shop:login')
    return render(request,'register.html')


def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,
                  user)
            return redirect('shop:categories')
        else:
            messages.error(request,"invalid credntials")
    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    return redirect('shop:login')

@login_required
def viewusers(request):
    k=Users.objects.all()
    context={'user':k}
    return render(request, 'viewusers.html',context)

@login_required
def user_orders(request):
    u=request.user
    orders = Order_details.objects.filter(user=u,payment_status="paid")
    context={'orders': orders}

    return render(request,'orders.html',context)



def add_product(request):

    if (request.method == "POST"):
        category_id = request.POST['c']

        n=request.POST['n']
        d= request.POST['d']
        p= request.POST['p']
        a= request.POST['a']

        c=request.FILES['i']

        g=Category.objects.get(id=category_id)



        b = Product.objects.create(name=n,desc=d,price=p,stock=a,category=g,image=c)
        b.save()
        return render(request, 'category.html')


    return render(request, 'add_product.html')




def add_cat(request):

    if (request.method == "POST"):
        t = request.POST['t']
        a = request.POST['a']
        c = request.FILES['i']


        b = Category.objects.create(name=t,desc=a,image=c)
        b.save()
        return render(request, 'category.html')

    return render(request, 'add_cat.html')

def add_stock(request,i):
    product=Product.objects.get(id=i)
    if (request.method == "POST"):
        product.stock=request.POST['s']
        product.save()
        return render(request, 'category.html')



    context = {'pro':product}
    return render(request,'add_stock.html',context)