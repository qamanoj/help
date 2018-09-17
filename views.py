from django.shortcuts import render,redirect
from .models import UserRegister
import datetime
import random
from utils.validation import ValidateInputs
from utils.email import mail

def user_register(request):
    if request.method == "POST":
        get = request.POST.get
        validate =  ValidateInputs()
        if 'user_register' in request.POST:
            firstname          = validate.str_strip_title_tags_sc(get('firstname'))
            lastname           = validate.str_strip_title_tags_sc(get('lastname'))
            number             = validate.str_strip_tags_sc(get('number'))
            email              = get('email')
            password           = validate.strong_password(get('password'))
            user_ip            = request.META['REMOTE_ADDR']
            user_register_time = datetime.datetime.now()
            print(firstname,lastname,number,email,password)
            obj = UserRegister(
            firstname=firstname,lastname=lastname,
            number=number,email=email,password=password,
            user_ip=user_ip,user_register_time=user_register_time
            )
            obj.save()
            return redirect("/login")

    return redirect("/")


def user_login(request):
    if request.method == "POST":
        get = request.POST.get
        validate =  ValidateInputs()
        if 'user_login' in request.POST:
            email              = get('email')
            password           = validate.strong_password(get('password'))
            print(password)
            user_ip            = request.META['REMOTE_ADDR']
            user_last_login_time = datetime.datetime.now()
            count = UserRegister.objects.filter(email=email,password=password).count()
            if count is 1:
                obj    = UserRegister.objects.filter(email=email,password=password)
                update = obj.update(user_ip=user_ip,user_last_login_time=user_last_login_time)
                record = UserRegister.objects.get(email=email,password=password)
                id     = record.id
                request.session['user_id'] = id
                print("all okk")
                return redirect("/")
            else:
                print("password didn't match")
                return redirect("/login")

    return redirect("/")

def user_logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect("/")


def user_forgot_password(request):
    if request.method == "POST":
        get = request.POST.get
        if 'submit' in request.POST:
            email = get("email")
            list=[]
            list.append(email)
            otp = random.randrange(1000,9999)
            request.session['user_otp'] = otp
            request.session['user_email'] = email
            mail(list,otp)
            return redirect("/verifyotp")
    return redirect("/")



def user_submit_otp(request):
    if request.method == "POST":
        get = request.POST.get
        if 'submit' in request.POST:
            otp = get("otp")
            user_otp = request.session['user_otp'] = otp
            if otp is user_otp:
                print(otp)
                return redirect("/resetpassword")
            else:
                return redirect("/verifyotp")
    return redirect("/")


def user_reset_otp(request):
    if request.method == "POST":
        validate =  ValidateInputs()
        get = request.POST.get
        if 'submit' in request.POST:
            new_password     = validate.strong_password(get('new_password'))
            conform_password = validate.strong_password(get('conform_password'))
            print(new_password," && ",conform_password)
            if new_password == conform_password:
                print('yes it is')
                email = request.session['user_email']
                obj = UserRegister.objects.filter(email=email)
                obj.update(password=conform_password)
                return redirect("/login")
            else:
                print('no')
                return redirect("/resetpassword")

    return redirect("/resetpassword")


obj = UserRegister.objects.filter(email="soubhagyakumar666@gmail.com")
obj.update(password=12345)

def view_user_profile(request):
    pass

def edit_user_profile(request):
    pass
