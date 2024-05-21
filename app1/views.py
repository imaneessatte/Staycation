from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login ,logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

# --------------- imported file from current dir -------------------------

from .models import House,Reservation,User
from .forms import HouseForm , ReservationForm ,UserForm 
from .decorators import unauthenticated_user,only_owners,only_clients


# LOGIN & LOGOUT ================================================================================

@unauthenticated_user
def loginPage(request):
    page ='login'
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        role = request.POST.get('role')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,'User does not exist!!')
        
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username or Password is incorrect !!')

    context = {'page':page}
    return render(request,'login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')


# REGISTRATION =========================================================================

@unauthenticated_user
def registerPage(request):
  
    form = UserForm()
    if request.method == 'POST':
        password = request.POST.get('password1')
        confirmation = request.POST.get('password2')
        role = request.POST.get('role')
        if password == confirmation:
            form = UserForm(request.POST)
            if form.is_valid():
                new_user =form.save(commit=False)
                new_user.username = new_user.username.lower()
                new_user.save()
                
                login(request,new_user)
                return redirect('home')
            else:
                messages.error(request,'Something went wrong please check your informations')
        else:
            messages.warning(request,"Password and Confirmation must be the same")
    context ={'form':form}
    return render(request,'login_register.html',context)

# MyHousses  PAGE ======================================================================

@login_required(login_url='login')
@only_owners
def myHouses(request):
    myHouses = House.objects.filter(owner = request.user)
    context = {'myHouses':myHouses}
    return render(request,'My_houses.html',context)

# HOME PAGE ============================================================================

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    w = request.GET.get('w') if request.GET.get('w') != None else '' 
    houses = House.objects.filter(Q(name__icontains=q) |
                                  Q(address__icontains=q) |
                                  Q(country__icontains=q) |
                                  Q(city__icontains=q) )
    distinct_country = House.objects.all().values_list('country',flat=True).distinct()
    distinct_city = House.objects.all().values_list('city',flat=True).distinct()

    housesByOwner = House.objects.filter()
    if houses is None:
        messages.info(request,'This search have no results')
    context = {'houses':houses,'distinct_country':distinct_country,'distinct_city':distinct_city}
    return render(request,'home.html',context)


# house CRUD------------------------------

@login_required(login_url='login')
@only_owners
def createHouse(request):
    form = HouseForm()
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = House.objects.create(
                owner = request.user,
                name = request.POST.get('name'),
                address = request.POST.get('address'),
                country = request.POST.get('country'),
                city = request.POST.get('city'),
                price = request.POST.get('price'),
                beds = request.POST.get('beds'),
                baths = request.POST.get('baths'),
                image = request.POST.get('image'),
                description = request.POST.get('description'),
            )
            house.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'house_form.html',context)

# ----------------------------------------

@login_required(login_url='login')
@only_owners
def updateHouse(request,pk):
    house = House.objects.get(id = pk)
    form = HouseForm(instance=house)
    if request.method == 'POST':
        form = HouseForm(request.POST,instance=house)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'house_form.html',context)

# ----------------------------------------

@login_required(login_url='login')
@only_owners
def deleteHouse(request,pk):
    house = House.objects.get(id = pk)

    if request.method == 'POST':
        house.delete()
        return redirect('home')
    context = {'obj':house}
    return render(request,'delete.html',context)


# RESERVATIONS PAGE ==================================================================

@login_required(login_url='login')
@only_clients
def reservations(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    reservations = Reservation.objects.filter(Q(house__name__icontains=q) |
                                  Q(house__address__icontains=q) |
                                  Q(house__country__icontains=q) |
                                  Q(house__city__icontains=q) )
    # Search by country and city -----------------------
    houses = House.objects.filter(Q(name__icontains=q) |
                                  Q(address__icontains=q) |
                                  Q(country__icontains=q) |
                                  Q(city__icontains=q) )
    
    distinct_country = House.objects.all().values_list('country',flat=True).distinct()
    distinct_city = House.objects.all().values_list('city',flat=True).distinct()
    context = {'reservations':reservations,'distinct_country':distinct_country,'distinct_city':distinct_city}
    return render(request,'reservations.html',context)

# Resevation CRUD ------------

@login_required(login_url='login')
@only_clients
def createReservation(request,pk):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = Reservation.objects.create(
                user = request.user,
                house = House.objects.get(id = pk),
                startDate = request.POST.get('startDate'),
                endDate = request.POST.get('endDate'),
            )
            reservation.save()
            # form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request,'reservation_form.html',context)

# ----------------------------------------

@login_required(login_url='login')
@only_clients
def updateReservation(request,pk):
    reservation = Reservation.objects.get(id = pk)
    form = ReservationForm(instance=reservation)
    
    if request.method == "POST":
        form = ReservationForm(request.POST,instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservations')
    context = {'form': form}
    return render(request,'reservation_form.html',context)

# ----------------------------------------

@login_required(login_url='login')
@only_clients
def deleteReservation(request,pk):
    reservation = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservations')
    context = {'obj': reservation}
    return render(request,'delete.html',context)


