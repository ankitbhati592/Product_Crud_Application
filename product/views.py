from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template import RequestContext
from django.template import Context
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from product.models import Product
from django.shortcuts import get_object_or_404
from product.forms import LoginForm
from django.core.files import File
import urllib


@login_required(login_url="/login/")
def home(request):
    """if not request.user.is_authenticated():
        return reverse("sign")
        user = product.objects.get(pk=id)
       current_user = User.objects.get(user=request.user)
       print current_user.id
       obj_user = User.objects.get(user=request.user)"""
    return render(request,"home.html")


@login_required(login_url="/login/")
def addproduct(request):
    return render(request, "product.html")

    if request.user.is_authenticated():
        return render(request, "home.html")


def signup(request):

    if request.method == "POST":
        form = Userform(request.POST)
        if form.is_valid():
            user = User.objects.create(

                Firstname=form.cleaned_data["Firstname"],
                Lastname=form.cleaned_data["Lastname"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            user.save()
            return redirect("/")
        else:
            return redirect(request, SignUp.html, {'form': form})
    return render(request, 'SignUp.html')

    """user=User.objects.create_user(**forms.cleaned_data)
            user.save()
            return redirect("/")
        else:
            error_message="please fill the valid detail"
            return redirect(request,'SignUp.html',{'form':form})
    else:
        error_message=""
        forms=Userform(use_required_attribute=False)
    return render(request,"SignUp.html",{'form':form,'error_message':error_message})"""


@login_required(login_url="/login/")
def delete(request, id):
    product = get_object_or_404(Product, pk=id).delete()
    return redirect("/productlisting/")


@login_required(login_url="/login/")
def update(request, id):
    prod_obj = Product.objects.get(pk=id)
    return render(request, "update.html", {'prod_obj': prod_obj})


@login_required(login_url="/login/")
def Updateproduct(request):
    id = request.POST.get('id', False)
    prod_obj = Product.objects.get(pk=id)
    prod_obj.productName = request.POST.get('pname', False)
    prod_obj.description = request.POST.get('des', False)
    prod_obj.quantity = request.POST.get('quan', False)
    prod_obj.price = request.POST.get('pri', False)
    prod_obj.phoneNumber = request.POST.get('phne', False)
    status = request.POST.get('status', False)
    if status == "1":
        prod_obj.status = True
    else:
        prod_obj.status = False
    image = request.FILES.get("pic")
    if image:
        prod_obj.image = image
    prod_obj.save()
    return redirect("/productlisting/")


@login_required(login_url="/login/")
def productinformation(request, id):
    product = Product.objects.get(pk=id)
    return render(request, "productinformation.html", {'product': product})


def sign(request):
    customer = User()
    customer.username = request.POST.get('Email', False)
    customer.set_password(request.POST.get('psw', False))
    customer.firstname = request.POST.get('fname', False)
    customer.lastname = request.POST.get('lname', False)
    customer.is_staff = 1
    customer.is_active = 1
    customer.save()
    return redirect('/')


@login_required(login_url="/login/")
def detailproduct(request):

    if request.user.is_authenticated():
        detail = Product()
        detail.productName = request.POST.get('pname', False)
        detail.description = request.POST.get('des', False)
        detail.quantity = request.POST.get('quan', False)
        detail.price = request.POST.get('pri', False)
        detail.phoneNumber = request.POST.get('phne', False)
        status = request.POST.get('status', False)
        detail.user = request.user
        if status == "1":
            detail.status = True
        else:
            detail.status = False
        detail.image = request.FILES.get("pic")
        detail.save()
        return redirect("/productlisting/")

    else:
        return redirect("/home/")


@login_required(login_url="/login/")
def productlisting(request):
    allProducts = Product.objects.filter(user= request.user)
    return render(request, "productlisting.html", {'allProducts': allProducts})
