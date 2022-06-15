from datetime import datetime
from email import message
import email
from re import template
from debugpy import configure
from django.dispatch import receiver
from matplotlib.style import use
from numpy import product
from requests import request
from store.decorators import unauthenticated_user
from store.models import Product
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json

#importam formularul din django

from django.contrib.auth.forms import UserCreationForm

#importam functia care apelaza cookies pentru checkout


#importam o functie pentru a face codul mai bine organizat

from .utils import cartData

#Cream views pentru login/ register

from .forms import OrderForm, CreateUserForm, ProductUserForm

#One time message pentru validarea unui cont nou

from django.contrib import messages

#Avem nevoie pentru a realiza operatiile de login si register

from django.contrib.auth import authenticate, login, logout

#Importam decoratorii

from .decorators import unauthenticated_user, allowed_users, admin_only

#Adaugam utilizatorul la un grup (admin/customer)

from django.contrib.auth.models import Group

#Adaugam functiile de filtrare

from .filters import ProductFilter

from .forms import *

#Importam librarie pentru trimiterea email-urilor

from django.core.mail import send_mail

from django.conf import settings

# Create your views here.

def store(request):
    
    #Se extrag datele din cos printr-o cerere catre server

    data = cartData(request)
    cartItems = data['cartItems']

    #Se extrag toate obiectele din tabelul cu produse

    products = Product.objects.all()

    #Se calculeaza toate reducerile
    
    context = {'products' : products, 'cartItems' : cartItems, 'shipping' : False}
    
    return render(request, 'store/store.html', context)

def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    for item in items:
        print(item.product.price - item.product.price * item.product.sales/100)
        item.product.price = item.product.price - item.product.price * item.product.sales/100

    context = { 'items' : items, 'order' : order, 'cartItems' : cartItems, 'shipping' : False}
    return render(request, 'store/cart.html', context)

def checkout(request):

    data = cartData(request)
    order = data['order']
    items = data['items']
    cartItems = data['cartItems']

    for item in items:
        print(item.product.price - item.product.price * item.product.sales/100)
        item.product.price = item.product.price - item.product.price * item.product.sales/100

    context = {'titlu':"Plata se face aici", 'order':order, 'items':items, 'cartItems':cartItems, 'shipping' : False}
    return render(request, 'store/checkout.html', context)

'''def charge(request):
    amount = 5
    if request.method == 'POST':
        print('Data', request.POST)

    return redirect(reverse('success', args = [amount]))'''

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)

def successMsg(request, args):
    amount = args
    return render(request, '/success.html', {'amount':amount})

# @allowed_users(allowed_roles= ['admin'])

def updateItem(request):
    data = json.loads(request.body)
    
    productId = data['productId']
    action = data['action']

    print('action',  action)
    print('product id', productId)

    customer = request.user.customer
    product = Product.objects.get(id = productId)

    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    print("natia matii", order)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

   #verificam ce tip de operatie a fost ceruta
    

    if action == "add":
        orderItem.quantity = orderItem.quantity + 1
    elif action == "remove":
        orderItem.quantity = orderItem.quantity - 1

    #retinem noua valoare a cantitatii din articol

    orderItem.save()

    #verificam daca mai sunt comandate produse de un anumit tip sau nu

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Articolul a fost adaugat", safe=False)

#@allowed_users(allowed_roles= ['admin'])

def description(request):
        data = cartData(request)
        cartItems = data['cartItems']

        products = Product.objects.all()

        myFilter =  ProductFilter(request.GET, queryset = products)

        products = myFilter.qs

        context = {'titlu':"Ceva", 'products' : products, 'cartItems' : cartItems, 'shipping' : False, 'myFilter': myFilter}
        
        return render(request, 'store/description.html', context)

@unauthenticated_user
#@allowed_users(allowed_roles= ['admin'])        

def loginPage(request):
        data = cartData(request)

        cartItems = data['cartItems']

        #Cream form-ul pentru autentificare

        form = CreateUserForm()

        #Extragem datele scrise in forma si le adaugam la back-end

        if request.method =="POST":

            #Extragem datele din casuta de login

            username = request.POST.get('username')
            password = request.POST.get('password')

            #Verificam daca datele sunt in baza de date

            user = authenticate(request, username = username, password = password)

            #Daca utilizatorul e in baza de date, dar nu e logat niciun cont, ii facem login

            if user is not None:
                login(request, user)

                #Cream customer


                return redirect('store')
            else:
                messages.info(request, 'Campul cu nume de utilizator sau cel cu parola lipseste sau este trecut incorect')

        context = {'cartItems' : cartItems, 'form':form}
        return render(request, 'store/login.html', context)

@unauthenticated_user
#@allowed_users(allowed_roles= ['admin'])

def register(request):

    data = cartData(request)

    cartItems = data['cartItems']

    #Cream form-ul pentru autentificare
    form = CreateUserForm()

    #Extragem datele scrise in forma si le adaugam la back-end

    if request.method =="POST":
        form = CreateUserForm(request.POST)
        #form = UserCreationForm(request.POST)
        
        #Validam datele introduse in form si le salvam

        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name = 'customer')
            user.groups.add(group)

            username = form.cleaned_data.get('username')

            customer = Customer(
                user = user,
                username = request.POST.get("username"),
                firstName = request.POST.get("firstName"),
                lastName = request.POST.get("lastName"),
                email = request.POST.get("email"),
                password1 = request.POST.get("password1"),
                password2 = request.POST.get("password2"),
            )

            customer.save()

            messages.success(request, 'Contul a fost creat cu succes pentru '+ username)

            return redirect('loginPage')

    context = {'cartItems' : cartItems, 'form':form}
    return render(request, 'store/register.html', context)

#@allowed_users(allowed_roles= ['admin'])

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

#@allowed_users(allowed_roles= ['customer'])

def profile(request, id):
    data = cartData(request)

    cartItems = data['cartItems']

    user = Customer.objects.filter(id = id).first()

    orders = Order.objects.all()

    customer = request.user.customer

    form = CustomerForm(instance= customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance= customer)
        if form.is_valid():
            form.save()

    context = {'cartItems' : cartItems, 'user': user, 'orders': orders, 'form': form}
    return render(request, 'store/profile.html', context)

#@allowed_users(allowed_roles= ['customer'])

def product(request, id):
    data = cartData(request)
    cartItems = data['cartItems']

    product = Product.objects.filter(id = id).first()

    reviews = ReviewProduct.objects.all()

    ingred = product.ingredients.split(",")

    alerg = product.alergens.split(",")

    discount = product.price - (product.sales*product.price/100)

    form = ReviewProductForm()

    if request.method == 'POST':
        print('Printing post', request.POST)
        form = ReviewProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('description')

    context = { 'product':product, 'cartItems' : cartItems, 'ingred': ingred, 'alerg' : alerg, 'discount': discount, 'form' : form, 'reviews': reviews }
    
    return render(request, 'store/product.html', context)

#@allowed_users(allowed_roles= ['admin'])

def special(request):
    data = cartData(request)
    cartItems = data['cartItems']

    form = ProductUserForm()

    products = Product.objects.all()

    if request.method == 'POST':
        print('Printing post', request.POST)
        form = ProductUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('store')
        #form.save()
        #send_mail("Contactat din partea ", message, settings.EMAIL_HOST_USER, ['oanasabina.iancu@outlook.com'], fail_silently = False )

    for product in products:
        if product.category == 'special':
            prod = product
            break

    context = { 'prod' : prod, 'cartItems' : cartItems, 'form': form }
    
    return render(request, 'store/special.html', context)

#@allowed_users(allowed_roles= ['admin'])

def recipes(request):

    data = cartData(request)
    cartItems = data['cartItems']

    recipes = Recipe.objects.all()

    nrrec = Recipe.objects.all().count()
    nrlist = []
    for i in range(nrrec):
        nrlist.append(i)
    print(nrlist)
    context = { 'recipes' : recipes, 'cartItems' : cartItems, "nrrec":nrrec}
    for i in recipes:
        print(i.imageURL)
    return render(request, 'store/recipes.html', context)

#@allowed_users(allowed_roles= ['admin'])

def recipe(request, id):
    data = cartData(request)
    cartItems = data['cartItems']

    recipe = Recipe.objects.filter(id = id).first()

    cakeing = recipe.cakeIng.split(",")
    creaming = recipe.creamIng.split(",")

    context = { 'recipe':recipe, 'cartItems' : cartItems, 'cakeing':cakeing, 'creaming':creaming }
    
    return render(request, 'store/recipe.html', context)

def presentation(request):
    data = cartData(request)
    cartItems = data['cartItems']

    
    context = { 'cartItems' : cartItems }
    
    return render(request, 'store/presentation.html', context)

def eroare(request, exception):
    data = cartData(request)
    cartItems = data['cartItems']


    context = { 'cartItems' : cartItems }

    return render(request, '404.html', context)

def error403(request):
    data = cartData(request)
    cartItems = data['cartItems']


    context = { 'cartItems' : cartItems }

    return render(request, 'error403.html', context) 

