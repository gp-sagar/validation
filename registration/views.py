import pkgutil
from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Device
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Sign Up page Logic

def signup(request):

    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['pass']
        c_password = request.POST['c_pass']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username is Already Taken') 
            return render(request, 'signup.html') 
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already in Use') 
                return render(request, 'signup.html') 
            else:
                if len(f_name) > 2:
                    if len(l_name) > 2:
                        if len(email) > 11:
                            if len(username) > 4:
                                if len(password) > 4:
                                    if password == c_password:
                                        addUser = User.objects.create_user(first_name=f_name, last_name=l_name, email=email, username=username, password=password)
                                        addUser.save()
                                        messages.success(request, 'Account created login now') 
                                        return redirect('/login')
                                    else:
                                        messages.info(request, 'Password not Matching')   
                                        return render(request, 'signup.html')
                                else:
                                    messages.info(request, 'Password is too sort')   
                                    return render(request, 'signup.html')
                            else:
                                messages.info(request, 'Username is minimum 5 Character')   
                                return render(request, 'signup.html')
                        else:
                            messages.info(request, 'Email is not valid')   
                            return render(request, 'signup.html')
                    else:
                        messages.info(request, 'Last name is too sort')   
                        return render(request, 'signup.html')
                else:
                    messages.info(request, 'First name is too sort')   
                    return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


# Login page Logic


def login(request):

    if request.method == 'POST':
        username = request.POST['l_username']
        password = request.POST['l_pass']

        if User.objects.filter(username=username).exists():

            log_user = auth.authenticate(username=username, password=password)

            if log_user is not None:
                auth.login(request, log_user)
                messages.success(request, 'Successfully login')
                return redirect('/welcome')
            else:
                messages.info(request, 'Password is Wrong')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Username is not Exist')
            return render(request, 'login.html')
            
    else:
        return render(request, 'login.html')


# Logout 
def logout(request):
    auth.logout(request)
    return redirect('/login')



# Welcome Page
@login_required(login_url='/login')
def welcome(request):
    data = Device.objects.all()
    return render(request, 'welcome.html', {'data': data})


# Add Device
@login_required(login_url='/login')
def addDevice(request):
    if request.method == 'POST':
        device_name = request.POST['deviceName']
        device_id = request.POST['deviceId']
        device_status = request.POST['deviceStatus']

        addDevice = Device(device_name=device_name, device_id=device_id, device_status=device_status)
        addDevice.save()
        messages.success(request, 'Device Added') 
        return redirect('/addDevice')
    else:
        return render(request, 'addDevice.html')

# Device Data
@login_required(login_url='/login')
def deviceData(request, id):
    devicepost = Device.objects.filter(id = id)[0]
    return render(request, 'deviceData.html', {'devicepost':devicepost})
