from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from shop.models import Product
from cart.models import Cart,Payment,Order_details
import razorpay
from django.contrib.auth.models import User
from django.contrib.auth import login
# Create your views here.

@login_required
def cart(request,i):
    p=Product.objects.get(id=i)
    u=request.user

    try:
        c=Cart.objects.get(user=u, product=p)
        if(p.stock>0):
            c.quantity += 1
            c.save()
            p.stock -= 1
            p.save()



    except:
        if(p.stock>0):
            c = Cart.objects.create(product=p, user=u, quantity=1)
            c.save()
            p.stock -= 1
            p.save()



    return redirect('cart:cartview')

@login_required()
def cart_view(request):
    u=request.user
    total=0
    c=Cart.objects.filter(user=u)
    for i in c:
        total+=i.quantity*i.product.price
    context={'cart':c,'total':total}
    return render(request,'cart.html',context)

@login_required()
def cart_remove(request,i):
    p=Product.objects.get(id=i)
    u=request.user

    try:
        c=Cart.objects.get(user=u,product=p)
        if(c.quantity>1):
            c.quantity-=1
            c.save()
            p.stock+=1
            p.save()
        else:
            c.delete()
            p.stock += 1
            p.save()

    except:
        pass

    return redirect('cart:cartview')
@login_required
def cart_delete(request,i):
    p = Product.objects.get(id=i)
    u = request.user

    try:
        c = Cart.objects.get(user=u, product=p)

        c.delete()
        p.stock+=c.quantity
        p.save()


    except:
        pass

    return redirect('cart:cartview')


@login_required
def orderform(request):
    if(request.method=="POST"):
          address=request.POST['a']
          phone=request.POST['p']
          pin=request.POST['pi']
          u=request.user
          c=Cart.objects.filter(user=u)

          total=0
          for i in c:


              total+=i.quantity*i.product.price
          total=int(total*100)

          client=razorpay.Client(auth=('rzp_test_UqQQNBiGHsRa3r','UqqteCrF4EDZXLrq2rnJXDPg'))#razropay id and scret key
          response_payment=client.order.create(dict(amount=total,currency="INR"))
          order_id = response_payment['id']
          order_status = response_payment['status']

          if order_status == "created":
              # Create the Payment entry
              p = Payment.objects.create(name=u.username, amount=total, order_id=order_id)

              # Create Order details for each item in the cart
              for i in c:
                  Order_details.objects.create(
                      product=i.product,
                      user=u,
                      no_of_items=i.quantity,
                      address=address,
                      phoneno=phone,
                      pin=pin,
                      order_id=order_id
                  )
          else:

              # Handle payment failure or non-creation of the order
              # Add logic here if you want to display an error or log it
              pass
          response_payment['name']=u.username
          context={'payment':response_payment}
          return render(request, 'payment.html',context)
    return render(request,'orderform.html')
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
@login_required
def payment_status(request,u):
    user=User.objects.get(username=u)
    if(not request.user.is_authenticated):
        login(request,user)
    if(request.method=="POST"):
        response=request.POST
        print(response)
        print(u)
        param_dict={
            'razorpay_order_id':response['razorpay_order_id'],
            'razorpay_payment_id':response['razorpay_payment_id'],
            'razorpay_signature':response['razorpay_signature']


        }
        client=razorpay.Client(auth=('rzp_test_UqQQNBiGHsRa3r','UqqteCrF4EDZXLrq2rnJXDPg'))
        try:
            status=client.utility.verify_payment_signature(param_dict)#to check authenticity of the razropay signature
            print(status)
            p=Payment.objects.get(order_id=response['razorpay_order_id'])
            p.razorpay_payment_id=response['razorpay_payment_id']
            p.paid=True
            p.save()


            user=User.objects.get(username=u)
            o=Order_details.objects.filter(user=user,order_id=response['razorpay_order_id'])
            for i in o:
                i.payment_status="paid"
                i.save()


            c=Cart.objects.filter(user=user)
            c.delete()
        except:
            pass
    return render(request,'payment_status.html',{'status':status})