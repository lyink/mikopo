from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .models import Location
from django.http import HttpResponse

# https://www.qstmsc.com/api/location.php

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Location  

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Location  

@csrf_exempt  
def receive_location(request):
    if request.method == 'POST':
        try:
            print("Received request body:", request.body)  
            data = json.loads(request.body)
            
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            address = data.get('address')
            android_id = str(data.get('id')).replace('.', '')  
            full_name = data.get('fullName')
            email = data.get('email')
            password = data.get('password')
            phone_number = data.get('phoneNumber')  

            if not all([latitude, longitude, address, android_id, full_name, email, password, phone_number]):
                return JsonResponse({'code': 400, 'message': 'Missing data'}, status=400)

            try:
                latitude = float(latitude)
                longitude = float(longitude)
            except ValueError:
                return JsonResponse({'code': 400, 'message': 'Invalid latitude or longitude'}, status=400)

            Location.objects.filter(android_id=android_id).delete()

            location = Location(
                latitude=latitude,
                longitude=longitude,
                location_address=address,
                android_id=android_id,
                full_name=full_name,
                email=email,
                password=password,
                phone_number=phone_number  
            )
            location.save()

            return JsonResponse({'code': 200, 'message': 'Location data saved successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'code': 400, 'message': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'code': 500, 'message': f'Error saving location data: {str(e)}'}, status=500)
    return JsonResponse({'code': 405, 'message': 'Method not allowed'}, status=405)



    


from django.shortcuts import render
from .models import Location  

def home(request):
  
    locations = Location.objects.all()
    
    context = {
        'locations': locations
    }
    
    return render(request, 'locations/home.html', context)


from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Location  

def home(request):

    locations = Location.objects.all()
    
    context = {
        'locations': locations
    }
    
    return render(request, 'locations/home.html', context)

def index(request):
    return render(request, 'locations/index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(reverse_lazy('index'))
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect(reverse_lazy('login'))


from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


from django.core.paginator import Paginator
from django.shortcuts import render

def registered_users(request):
 
    user_list = [
        {'Company': 'Alfreds Futterkiste', 'Contact': 'Maria Anders', 'Country': 'Germany'},
        {'Company': 'Centro comercial Moctezuma', 'Contact': 'Francisco Chang', 'Country': 'Mexico'},
        {'Company': 'Ernst Handel', 'Contact': 'Roland Mendel', 'Country': 'Austria'},
        {'Company': 'Island Trading', 'Contact': 'Helen Bennett', 'Country': 'UK'},
        {'Company': 'Laughing Bacchus Winecellars', 'Contact': 'Yoshi Tannamuri', 'Country': 'Canada'},
        {'Company': 'Magazzini Alimentari Riuniti', 'Contact': 'Giovanni Rovelli', 'Country': 'Italy'},
      
    ]

    paginator = Paginator(user_list, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'locations/registered_users.html', {'page_obj': page_obj})


def devices_location(request):
    return render(request, 'locations/devices_location.html')   

def lost_devices(request):
    return render(request, 'locations/lost_devices.html')   

def last_location(request):
    return render(request, 'locations/last_location.html')   


def devices_location(request):
    return render(request, 'locations/devices_location.html')  















