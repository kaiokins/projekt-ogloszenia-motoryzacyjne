from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from cars.models import Car
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Zalogowałeś się')
            return redirect('panel')
        else:
            messages.error(request, 'Nieprawidłowy login')
            return redirect('login')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Użytkownik istnieje')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email istnieje')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'Zalogowałeś się')
                    return redirect('panel')
                    user.save()
                    messages.success(request, 'Zarejestrowano się pomyślnie')
                    return redirect('login')
        else:
            messages.error(request, 'Hasła są różne')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

@login_required(login_url = 'login')
def panel(request):
    car = Car.objects.order_by('-added')
    userQuestion = Contact.objects.order_by('-added').filter(userId=request.user.id)
    data = {'userQuestion' : userQuestion, 'car': car}
    return render(request, 'accounts/panel.html', data)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Zostałeś wylogowany')
        return redirect('home')
    return redirect('home')