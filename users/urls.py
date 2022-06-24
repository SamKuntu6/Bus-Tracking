from django.urls import path
from . import views


app_name = "users"
urlpatterns = [
	
	path('', views.HomeView.as_view(), name="home"),
	path('sign-in', views.login_page, name="sign-in"),
	path('sign-out', views.sign_out, name="sign-out"),
	path('studentcreate', views.student_create, name="student_create"),
	path('studentview', views.student_view, name="student_view"),
]

# Remain here for future

# path('sign-up', views.register_page, name="sign-up"),
# path('profile', views.profile_view, name="stud_profile"),