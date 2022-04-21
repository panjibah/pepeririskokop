from django.shortcuts import render
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user,allowed_users
from users.models import CustomUser
from django.db import connection, reset_queries
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db import connection  
import logging
import json
import datetime
from django.contrib.auth.models import Group
from django.contrib import messages
from .decorators import unauthenticated_user,allowed_users




def loginUser (request): 
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            context = {
                "messages":"creddential not exist",
            }   
            return render(request,'users/login.html',context)

    if request.method =='POST':
        print("masuk")
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            # print(request.user.is_approver)
            # print(request.user.is_operator)
            context = {
                "messages":"success",
            }
            # print(dict(request.POST.items()))
            # #inser roles to dict
            # group = request.user.groups.all()
            # roles = []
            # for g in group:
            #     roles.append(g.name)
            # print(type(group))
            
            # user_detail = {
            #     "roles":roles
            # }
            
        
            return redirect('dashboard')

        else:
            context = {
                "messages":"creddential not exist",
            }
            print(dict(request.POST.items()))
            return render(request,'users/login.html',context)
    else:
        context = {
                "messages":"",
            }
        return render(request,'users/login.html',context)
    
def logoutUser(request):
    #inser roles to dict
    group = request.user.groups.all()
    roles = []
    for g in group:
        roles.append(g.name)
    print(type(group))
    
    user_detail = {
        "roles":roles
    }
    
    #Log logout
    # raLog = AuditLog(
    # user_id =request.user,
    # data_id = request.user.id,
    # old_data = None,
    # new_data = user_detail,
    # table   ="User",
    # message ="Logout User",
    # description = request.user.first_name,
    # )
    # raLog.save()
    logout(request)
    context = {"messages":"",
            }
    return redirect ('loginUser')


def registerUser (request):

    if request.POST:
        username = request.POST['username']
        name = request.POST['name']
        isOperator=request.POST.get('operator',False)
        isSupervisor = request.POST.get('supervisor',False)
        isAdmin = request.POST.get('admin',False)
        isSuperAdmin = request.POST.get('superAdmin',False)
        email = ''
        # password = request.POST['password1']
        
        
        #check duplicate username
        chkUsername = CustomUser.objects.filter(username__icontains = username)
        print(chkUsername.count())
        if(chkUsername):
            messages.info(request,"Username Already Exist")
            return redirect(registerUser)
        
        #SET DEFAULT PASSWORD
        password = username + '2021'
        print(type(password))
        user = get_user_model().objects.create(username=username,email=email,)
        user.set_password(password)
        user.first_name = name
        user.save() 
        
        #SET USER ROLES
        # user = CustomUser.objects.latest('id')
        # if isOperator == "on" :
        #     my_group = Group.objects.get(name='Operator') 
        #     my_group.user_set.add(user)

        # if isSupervisor == "on" :
        #     my_group = Group.objects.get(name='Supervisor') 
        #     my_group.user_set.add(user)
       
        # if isAdmin== "on" :
        #     my_group = Group.objects.get(name='Admin') 
        #     my_group.user_set.add(user)

        # if isSuperAdmin == "on" :
        #     my_group = Group.objects.get(name='SuperAdmin') 
        #     my_group.user_set.add(user)

        
        #log manual to file
        # logDict = {
        # "userID":request.user.id,
        # "dates" :datetime.datetime.now(),
        # "query" :'connection.queries[0]',
        # "recordsData": CustomUser.objects.latest('id'),
        # "messages"  : 'User Created'
        # }
        #Log to database
        # newUser =CustomUser.objects.latest('id')
        # raLog = AuditLog(
        #     user_id =request.user,
        #     data_id = newUser.id,
        #     old_data = None,
        #     new_data = newUser,
        #     table   ="User",
        #     message ="Create User",
        #     description = newUser.first_name
        # )
        # raLog.save()
        
        # logJson = json.dumps(logDict,default=str)
        # logger.info(logJson)
        
        print(dict(request.POST.items()))
        
    context={
   
    }
    return render(request,'users/register.html',context)