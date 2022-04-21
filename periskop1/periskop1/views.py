from django.db import connection, reset_queries
from django.shortcuts import render,redirect
from django.contrib.auth.models import Group
from django.db import connection  
import logging
import json
import datetime
from django.contrib.auth.models import Group
from django.contrib.auth.models import Group
from users.decorators import unauthenticated_user,allowed_users

@unauthenticated_user
def base(request):
    print("ss")
    return render(request,'base.html')