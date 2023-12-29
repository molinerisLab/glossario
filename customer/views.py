from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.conf import settings
import re

def create_user_by_email(email,first_name=None, last_name=None, is_staff=False, groups=[]):
    email = email.strip().lower()
    try:
        user = User.objects.get(email=email)
    except:
        user = User.objects.create_user(username=email, email=email, is_staff=is_staff)
        if first_name:
            user.first_name=first_name
        if last_name:
            user.last_name=last_name
        #user.set_password(settings.CUSTOMER_DEFAULT_PSW)
    for g in groups:
        g = Group.objects.get(name=g) 
        g.user_set.add(user)
    user.save()
    return user

def validate_simple_name(value):
    if not re.match(r"^[A-Za-z0-9]+$",value):
        raise ValidationError('the value "%s" is not a valid, use only alphanumeric character.' % value)

