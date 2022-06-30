from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from .forms import UserForm
from django.contrib import messages
from .models import *
from main.models import *
from bustracking.decorators import unauthenticated_user

# firebase imports and initialization
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("bustracking/ServiceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
# end firebase imports


from bustracking.mixins import(
	AjaxFormMixin, 
	FormErrors,
	RedirectParams,
	)


from .forms import (
	UserForm,
	UserProfileForm,
	AuthForm,
	)

result = "Error"
message = "There was an error, please try again"


class HomeView(TemplateView):
	'''
	Generic FormView with our mixin to display user account page
	'''
	template_name = "users/index.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		context = super(HomeView, self).dispatch(*args, **kwargs)
		context['trips'] = Trip.objects.all()
		
		return context



def login_page(request):
	'''
	Basic view for user sign in without form validation
	'''
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'users/login.html', context)



def sign_out(request):
	'''
	Basic view for user sign out
	'''
	logout(request)
	return redirect(reverse('users:sign-in'))


@login_required(login_url='users:sign-in')
def student_create(request):
	students_users = User.objects.filter(username__startswith = "stud")
	students_list = []
	
	for student in students_users:
		stud_str = student.get_full_name()
		students_list.append(stud_str)
	
	# chosen_user = request.POST.get('name')
	
	# found_user = User.objects.filter(full_name = chosen_user)
	
	form = UserProfileForm() 

	if request.is_ajax():
		form = UserProfileForm(data = request.POST)
		if form.is_valid():
			obj = form.save()
			obj.has_profile = True
			obj.save()
			result = "Success"
			message = "Your profile has been updated"
		else:
			message = FormErrors(form)
		data = {'result': result, 'message': message}
		return JsonResponse(data)
	else:
		context = {'form': form}

	chosen_user = request.POST.get('stud')
	stud_class = request.POST.get('class')
	parent_name = request.POST.get('par-name')
	relation = request.POST.get('relation')
	phone = request.POST.get('phone')
	email = request.POST.get('email')

	# Student.objects.create(
	# 		stud_name=chosen_user,
	# 		parent_name=parent_name,
	# 		relationship=relation,
	# 		classroom=stud_class,
	# 		parent_phone=phone,
	# 		email=email,
	# 	)

	context = {"students":students_list,
	"google_api_key": settings.GOOGLE_API_KEY,
	"base_country": settings.BASE_COUNTRY}
	return render(request, 'users/studentcreate.html', context)


@login_required(login_url='users:sign-in')
def student_view(request):
	# for only this web database
	all_students = Student.objects.all().values()
	
	# for firestore connection
	# list_students = []
	# all_firestore_students = db.collection('students').get()
	# for student in all_firestore_students:
	# 	list_students.append(student.to_dict())
	

	context = {
		'students': all_students,
		# 'fire_studs': list_students
		}
	return render(request, 'users/studentview.html', context)


def delete_student(request, pk):
	# for only this web database
	student = Student.objects.get(id=pk)
	student.delete()
	messages.success(request, 'Student Info deleted successfully!')

	# for firestore connection
	return redirect('users:student_view')


def update_student(request, pk):
	# for only this web database

	if Student.objects.filter(id=pk).exists():
		chosen_stud = request.POST.get('stud')
		stud_class = request.POST.get('class')
		parent_name = request.POST.get('par-name')
		relation = request.POST.get('relation')
		phone = request.POST.get('phone')
		email = request.POST.get('email')

		Student.objects.filter(id=pk).update(
			stud_name=chosen_stud,
			parent_name=parent_name,
			relationship=relation,
			classroom=stud_class,
			parent_phone=phone,
			email=email,
		)

	# for firestore connection

	return redirect('users:student_view')
