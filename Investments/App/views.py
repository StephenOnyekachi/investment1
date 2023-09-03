import random
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Plans
from .models import Users
from .models import Messages
from .models import Histories

# Create your views here.

def UserLogout(request):
    logout(request)
    return redirect('user_login')

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('adminview')
            else:
                login(request, user)
                return redirect('dashboard')
        else:
            messages.info(request, 'username or password is incorrect')
            return redirect('login')
    context = {
        'message': messages,
    }
    return render(request, 'login.html', context)


def Index(request):
    plan = Plans.objects.all()
    context = {
        'plan': plan,
    }
    return render(request, 'index.html', context)


def SignUp(request):
    if request.method == 'POST':
        username = request.POST['name']
        number = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if Users.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else:
                Users.objects.create_user(
                    username = username,
                    number = number,
                    password = password1,
                )

                messages.success(request, 'User was successfully')
                return redirect('login')
        else:
            messages.info(request, 'password not matching...')
            return redirect('newuser') 
    context = {
        # 'plans': plans,
    }
    return render(request, 'signup.html', context)


@login_required(login_url='login')
def AdminView(request):
    user = Users.objects.filter(is_superuser=False).order_by('-id')
    message = Messages.objects.all().order_by('-id')
    history = Histories.objects.all().order_by('-id')
    plan = Plans.objects.all().order_by('-id')
    context = {
        'user': user,
        'message': message,
        'history': history,
        'plan': plan
    }
    return render(request, 'admin.html', context)


@login_required(login_url='login')
def Approve(request, pk):
    user = Histories.objects.get(id=pk)
    if request.method == 'POST':
        approve = request.POST['approve']
        user.status = approve
        user.save()
        messages.success(request, 'Updates was successful')
        return redirect('adminview')
    context = {
        'user':user,
    }
    return render(request, 'approve.html', context)


@login_required(login_url='login')
def EditUser(request, pk):
    user = Users.objects.get(id=pk)
    plan = Plans.objects.all()
    if request.method == 'POST':
        plan = request.POST['plan']
        price = request.POST['price']
        parcent = request.POST['parcent']
        user.plan = plan
        user.parcent = parcent
        user.price = price
        user.balance = int(parcent) + int(price)
        user.save()
        messages.success(request, 'Updates was successful')
        return redirect('adminview')
    context = {
        'user':user,
        'plan':plan,
    }
    return render(request, 'edit.html', context)


@login_required(login_url='login')
def DeleteUser(request, pk):
    user = Users.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Updates was successful')
        return redirect('adminview')
    context = {
        'user':user,
    }
    return render(request, 'delete.html', context)


@login_required(login_url='user_login')
def Block(request, pk):
    user = Users.objects.get(id=pk)
    if request.method == 'POST':

        if user.block:
            user.block = False
            user.save()
            return redirect('adminview')

        user.block = True
        user.save()
        return redirect('adminview')
    context = {
        'user': user,
    }
    return render(request, 'block.html', context)
    

@login_required(login_url='login')
def DashboardView(request):
    user = request.user
    balance = user.price
    # parcent = user.parcent

    # total = int(parcent)
    total = int(balance)
    if request.method == 'POST':
        user = request.user
        parcent = request.POST['parcent']

        user.balance += float(parcent)
        user.save()
        messages.success(request,'Your Just Earnd Todays Commision')
        return redirect('dashboard')
    
    context = {
        'user': user,
        'total':total,
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def Withdraw(request):
    if request.method == 'POST':
        # search = request.POST.get('search')
        user = request.user
        # print(search)
        amount = request.POST['amount']
        if user.balance < int(amount):
            messages.info(request, 'insufficient balance try again')
            return redirect('withdraw')
        else:
            user.balance -= int(amount)
            user.save()

            user_name = user.username
            user_amount = amount

            history = Histories.objects.create(status=user_name, amount=user_amount,)
            history.save()
            messages.info(request, 'Withdraw Application Was successfully')
            return redirect('dashboard')

    context = {
        # 'plans': plans,
    }
    return render(request, 'withdraw.html', context)


@login_required(login_url='login')
def Upgrade(request):
    plan = Plans.objects.all()
    context = {
        'plan': plan,
    }
    return render(request, 'upgrade.html', context)


@login_required(login_url='login')
def PlanEdit(request, pk):
    user = Plans.objects.get(id=pk)
    if request.method == 'POST':
        plan = request.POST['plan']
        price = request.POST['price']
        parcent = request.POST['parcent']
        user.name = plan
        user.parcentage = parcent
        user.price = price
        user.save()
        messages.success(request, 'Updates was successful')
        return redirect('adminview')
    context = {
        'user':user,
    }
    return render(request, 'planedit.html', context)


@login_required(login_url='login')
def PlanDelete(request, pk):
    user = Plans.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Updates was successful')
        return redirect('adminview')
    context = {
        'user':user,
    }
    return render(request, 'plandelete.html', context)


@login_required(login_url='login')
def Payment(request, pk):
    plan = Plans.objects.get(id=pk)
    context = {
        'plan': plan,
    }
    return render(request, 'paymentinfo.html', context)


@login_required(login_url='login')
def Mes(request):
    message = Messages.objects.all().order_by('-id')
    
    context = {
        'message': message,
        # 'hihistory':history,
    }
    return render(request, 'mes.html', context)


@login_required(login_url='login')
def Sms(request):
    user = request.user
    message = Messages.objects.all().order_by('-id')
    # history = Histories.objects.all().order_by('-id')
    if request.method == 'POST':
        message = request.POST['message']
        picture = request.FILES.get('file')
        name = user.username

        message = Messages.objects.create(
            message=message, name=name, picture=picture
        )
        messages.success(request, 'Message Was Sent successful')
        return redirect('dashboard')
    
    context = {
        'message': message,
        # 'hihistory':history,
    }
    messages.success
    return render(request, 'sendmes.html', context)


@login_required(login_url='login')
def Bankinfo(request):
    context = {
        # 'plans': plans,
    }
    return render(request, 'info.html', context)


@login_required(login_url='login')
def Userinfo(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'userinfo.html', context)


@login_required(login_url='login')
def History(request):
    history = Histories.objects.all().order_by('-id')
    context = {
        'history':history,
    }
    return render(request, 'history.html', context)

