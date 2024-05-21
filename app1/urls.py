from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('home/',views.home,name='home'),
    path('My-houses/',views.myHouses,name="My-houses"),
    path('create-house/',views.createHouse,name='create-house'),
    path('update-house/<str:pk>/',views.updateHouse,name='update-house'),
    path('delete-house/<str:pk>/',views.deleteHouse,name='delete-house'),
    path('reservations/',views.reservations,name='reservations'),
    path('create-reservation/<str:pk>/',views.createReservation,name='create-reservation'),
    path('update-reservation/<str:pk>/',views.updateReservation,name='update-reservation'),
    path('delete-reservation/<str:pk>/',views.deleteReservation,name='delete-reservation'),
]