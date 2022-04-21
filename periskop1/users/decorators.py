from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request,*args,**kwargs)
        else:
            return redirect('loginUser')

    return wrapper_func


def allowed_users2(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                #only check first group
                group  = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs) 
            else:
                return redirect('unfinishedRA')
               
        return wrapper_func
    return decorator
    
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group = False
            groupSize = len(allowed_roles)
            for g in allowed_roles:
                if request.user.groups.filter(name=g).exists():
                    group = True
            if group == True:
                return view_func(request,*args,**kwargs) 
            else:
                return redirect('unfinishedRA')
        return wrapper_func
    return decorator
    