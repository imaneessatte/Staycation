from django.contrib import admin
from .models import House , Reservation , User
# Register your models here.

admin.site.register(House)
admin.site.register(Reservation)
admin.site.register(User)