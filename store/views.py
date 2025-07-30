from django.shortcuts import render,redirect,HttpResponse
from django.http.response import JsonResponse
from .models import *
import random
from .models import Cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse

# def main(request):
#     Catagory = catagory.objects.all()
#     context = {'Catagory':Catagory}
#     return render(request , "index.html", context)

@login_required(login_url='signin')
def home(request):
    Catagory = catagory.objects.all()
    Slide1= slide1.objects.all()
    Slide2= slide2.objects.all()
    Slide3= slide4.objects.all()
    Slide4= slide1.objects.all()
    context = {'Catagory':Catagory, 'Slide1':Slide1,'Slide2':Slide2,'Slide3':Slide3,'Slide4':Slide4}
    return render(request, "index.html", context)


@login_required(login_url='signin')
def collection(request, cslug):
    if(product.objects.filter(slug=cslug)):
        Product = product.objects.filter(slug=cslug)
        # Catagory = catagory.objects.filter(slug = cslug)
        context = {'Product':Product}
    return render(request, "collections.html", context)

@login_required(login_url='signin')
def ok(request, prod_name ,pslug):
        if(product.objects.filter(name=prod_name)): 
            Product = product.objects.filter(name=prod_name)
            Pro = product.objects.filter(slug=pslug)
            context = {'Product':Product , 'Pro':Pro}
        return render(request , "product.html", context)



def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Your password not matched")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('signin')
    
    return render(request, 'signup.html')
    


def signin(request):
    if request.method=='POST':
        user=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=user, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("username or password not matched")
        
    return render(request, 'signin.html')



def Logout(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def addto(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            product_id = int(request.POST.get('product_name'))
            product_check = product.objects.get(id=product_id)
            qty = request.POST.get('product_qty')
            if (product_check):
                if(Cart.objects.filter(user= request.user, product_id=product_id)):
                    return JsonResponse({'status':"product is already in cart"})
                else:                  
                    # if product_check.quantity >= qty:
                    Cart.objects.create(user= request.user, product_id=product_id, product_qty = qty)
                    
    
    return redirect('/')


@login_required(login_url='signin')
def cart(request):
    cart= Cart.objects.filter(user=request.user)
    # cartitems = Cart.objects.filter(user= request.user)
    totalprice = 0
    for item in cart:
        totalprice = totalprice + item.product.selling_price*item.product_qty
    context = {'cart': cart , 'totalprice': totalprice}
    return render(request , "cart.html", context)
    


def delete(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id =prod_id)):
            cartItem = Cart.objects.get(product_id= prod_id, user= request.user)
            
            cartItem.delete()
            
    return redirect('/')        
        

@login_required(login_url='signin')  
def checkout(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id = item.id)
    
    cartitems = Cart.objects.filter(user= request.user)
    totalprice = 0
    for item in cartitems:
        totalprice = totalprice + item.product.selling_price*item.product_qty
    
    userprofile=Profile.objects.filter(user=request.user)

    context = {'cartitems': cartitems, 'totalprice': totalprice, 'userprofile': userprofile}
    return render(request, 'checkoutPage.html', context)


@login_required(login_url='signin')
def placeorder(request):
    if request.method == 'POST':

        currentuser = User.objects.filter(id=request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('name')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user=request.user
            userprofile.phone = request.POST.get('phone')
            userprofile.city = request.POST.get('city')
            userprofile.pincode = request.POST.get('pin')
            userprofile.area = request.POST.get('area')
            userprofile.house_name = request.POST.get('hname')
            userprofile.save()


        neworder = Order()
        neworder.user = request.user
        neworder.name = request.POST.get('name')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.city = request.POST.get('city')
        neworder.pincode = request.POST.get('pin')
        neworder.area = request.POST.get('area')
        neworder.house_name = request.POST.get('hname')
        # neworder.total_price = request.POST.get('name')

        neworder.payment_mode = request.POST.get('payment_mode')

        cart = Cart.objects.filter(user= request.user)
        cart_total_price = 0

        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price*item.product_qty
            neworder.total_price = cart_total_price
            trackno = 'cMar' + str(random.randint(111111,999999))
            while Order.objects.filter(tracking_no = trackno) is None:
                trackno = 'cMar' + str(random.randint(111111,999999))

            neworder.tracking_no=trackno
            neworder.save()

            neworderitems = Cart.objects.filter(user = request.user)
            for item in neworderitems:
                OrderItem.objects.create(
                    order = neworder,
                    product = item.product,
                    price = item.product.selling_price,
                    quantity = item.product_qty
                )

                # to decrease the product quantity in available store
                orderproduct = product.objects.filter(id=item.product_id).first()
                orderproduct.quantity = orderproduct.quantity - item.product_qty
                orderproduct.save()

            #to clear user cart

            Cart.objects.filter(user = request.user).delete()
            messages.success(request, "Your order has been placed successfully")


    return redirect ('/')        

def myorders(request):
    orders = Order.objects.filter(user= request.user)
    context = {'orders': orders}
    return render(request, "orderview.html" , context)

def orderview(request, t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = {'order':order, 'orderitems': orderitems}
    return render(request, "track.html", context)

def productlistajax(request):
    products = product.objects.filter(status=0).values_list('name',flat=True)
    productList = list(products)

    return JsonResponse(productList,safe= False)

def searchproduct(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            products = product.objects.filter(name__contains = searchedterm).first()

            if products:
                return redirect("collections/"+product.name+'/'+product.slug)
            else:
                return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))