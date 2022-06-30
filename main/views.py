from multiprocessing import Condition
from tkinter import TRUE
from unicodedata import name
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib.auth.models import User
from bustracking.mixins import Directions
from users.models import *
from main.models import *
from bustracking.decorators import unauthenticated_user
from django.views import View
from django.template import loader
from django.contrib import messages


'''
Basic view for routing 
'''
def create_route(request):

	print("Upo hapo")
	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"base_country": settings.BASE_COUNTRY}
	return render(request, 'main/createroutes.html', context)


'''
Basic view for displaying a map 
'''
def directions(request):

	lat_a = request.GET.get("lat_a", None)
	long_a = request.GET.get("long_a", None)
	lat_b = request.GET.get("lat_b", None)
	long_b = request.GET.get("long_b", None)
	lat_c = request.GET.get("lat_c", None)
	long_c = request.GET.get("long_c", None)
	lat_d = request.GET.get("lat_d", None)
	long_d = request.GET.get("long_d", None)
	lat_e = request.GET.get("lat_e", None)
	long_e = request.GET.get("long_e", None)
	lat_f = request.GET.get("lat_f", None)
	long_f = request.GET.get("long_f", None)
	lat_g = request.GET.get("lat_g", None)
	long_g = request.GET.get("long_g", None)

	#only call API if all 7 addresses are added
	if lat_a and lat_b and lat_c and lat_d and lat_e and lat_f and lat_g:
		directions = Directions(
			lat_a= lat_a,
			long_a=long_a,
			lat_b = lat_b,
			long_b=long_b,
			lat_c= lat_c,
			long_c=long_c,
			lat_d = lat_d,
			long_d=long_d,
			lat_e = lat_e,
			long_e = long_e,
			lat_f = lat_f,
			long_f = long_f,
			lat_g = lat_g,
			long_g = long_g,
			)
	else:
		pass
		# return redirect(reverse('main:create_route'))

	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"base_country": settings.BASE_COUNTRY,
	"lat_a": lat_a,
	"long_a": long_a,
	"lat_b": lat_b,
	"long_b": long_b,
	"lat_c": lat_c,
	"long_c": long_c,
	"lat_d": lat_d,
	"long_d": long_d,
	"lat_e": lat_e,
	"long_e": long_e,
	"lat_f": lat_f,
	"long_f": long_f,
	"lat_g": lat_g,
	"long_g": long_g,
	"origin": f'{lat_a}, {long_a}',
	"destination": f'{lat_g}, {long_g}',
	# "directions": directions,

	}
	return render(request, 'main/routesdirection.html', context)


def home(request):
	busses = Buss.objects.all().values('plate_no', 'driver_assigned', 'attendant_assigned', 'capacity',
	 'condition', 'status', 'current_address')
	print(busses)
	context = {'busses': busses}
	return render(request, 'main/index.html', context)


def bus_create(request):
	# for only this web database
		# Values to send to the view 
	attendant_users = Employee.objects.exclude(type = "Driver").values('name')
	driver_users = Employee.objects.exclude(type = "Attendant").values('name')
	driver_list = []
	attendant_list = []

	for drv in driver_users:
		driver_list.append(drv['name'])
	
	for attend in attendant_users:
		attendant_list.append(attend['name'])

	# Saving to the Database
	if request.method == 'POST':
		plate_no = request.POST.get('plate_no')
		driver = request.POST.get('driver')
		attendant = request.POST.get('attendant')
		capacity = request.POST.get('capacity')

		Buss.objects.create(
			plate_no= plate_no,
			driver_assigned=driver,
			attendant_assigned=attendant,
			capacity=capacity,
			)
		return redirect('main:bus_create')
	
	# for firestore connections and updates

	context = {
		'attendants':attendant_list,
		'drivers': driver_list
	}
	return render(request, 'main/buscreate.html', context)



def bus_view(request):
	# for this web database only
		# Values to send to the view 
	attendant_users = Employee.objects.exclude(type = "Driver").values('name')
	driver_users = Employee.objects.exclude(type = "Attendant").values('name')
	driver_list = []
	attendant_list = []

	for drv in driver_users:
		driver_list.append(drv['name'])
	
	for attend in attendant_users:
		attendant_list.append(attend['name'])
		
	busses = Buss.objects.all().values('id', 'plate_no', 'driver_assigned', 'attendant_assigned', 'capacity',
	'condition', 'status', 'current_address')

	# for firestore connections and fetching

	context = {
		'busses': busses,
		'attendants':attendant_list,
		'drivers': driver_list
		}
	return render(request, 'main/busview.html', context)



def deletebus(request, pk):
	# for only this web database
	bus = Buss.objects.filter(id=pk)
	bus.delete()
	messages.success(request, 'Bus Info deleted successfully!')

	# for firestore connection
	return redirect('main:bus_view')



def updatebus(request, pk):
	# for only this web database
	if Buss.objects.filter(id=pk).exists():
		plate_no = request.POST.get('plate_no')
		driver = request.POST.get('driver')
		attendant = request.POST.get('attendant')
		capacity = request.POST.get('capacity')
		state = request.POST.get('state')

		Buss.objects.filter(id=pk).update(
			plate_no= plate_no,
			driver_assigned=driver,
			attendant_assigned=attendant,
			capacity=capacity,
			status=state,
		)

	# for firestore updates
	return redirect('main:bus_view')



# for future creation
def settings_view(request):
	return render(request, 'main/settings.html')



def emergency_view(request):
	# for only this web database
	busses_emergency = Buss.objects.filter(condition = True).values()
	# obj.last_accessed = timezone.now()

	# for firestore connections and updates

	context = {'busses': busses_emergency}
	return render(request, 'main/emergency.html', context)
	