
from django.contrib.auth.decorators import login_required

from django.contrib import messages


from django.shortcuts import render, redirect
def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

from django.contrib.auth.forms import UserCreationForm



from django.contrib.auth import logout

def force_logout(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            print("Form errors:", form.errors)  # Debug
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


