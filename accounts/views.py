from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        print('metoda post')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def panel(request):
    return render(request, 'accounts/panel.html')

def logout(request):
    return render(request, 'pages/home.html') # Tutaj trzeba będzie to naprawić