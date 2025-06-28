
from django.contrib.auth.decorators import login_required

from django.contrib import messages


from django.shortcuts import render, redirect
def home(request):
    return render(request, 'home.html')

from .models import WarrantyItem  # Import your model
@login_required
def dashboard(request):
    items = WarrantyItem.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'items': items})


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



from .forms import WarrantyItemForm
from django.contrib.auth.decorators import login_required

@login_required
@login_required
def upload_warranty(request):
    if request.method == 'POST':
        form = WarrantyItemForm(request.POST, request.FILES)
        if form.is_valid():
            warranty = form.save(commit=False)
            warranty.user = request.user
            warranty.save()
            messages.success(request, "Warranty item uploaded successfully.")
            return redirect('dashboard')
    else:
        form = WarrantyItemForm()
    return render(request, 'upload_warranty_item.html', {'form': form})


