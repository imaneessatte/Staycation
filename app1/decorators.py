# ----------------- import files -----------------------
from django.http import HttpResponse
from django.shortcuts import redirect

# ---------------- Testing if a user is authenticated or not ------------------------
def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

# ---------------- Restricting user permissions for only Owners ------------------------
def only_owners(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.role == 'Owner' :
            return view_func(request,*args,**kwargs)
        else:
            return redirect('home')
    return wrapper_func

# ---------------- Restricting user permissions for only Clients ------------------------
def only_clients(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.role == 'Client':
            return view_func(request,*args,**kwargs)
        else:
            return redirect('home')
    return wrapper_func

# ---------------- Restricting user permissions for only admin ------------------------
# def only_admin(view_func):
#     def wrapper_func(request,*args,**kwargs):
#         if  :
#             return view_func(request,*args,**kwargs)
#         else:
#             return redirect('home')
#     return wrapper_func

