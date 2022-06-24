from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    # path('route', views.route, name="route"),
    # path('map', views.map, name="map"),
    # path('index', views.home, name="home"),
    path('buscreate', views.bus_create, name="bus_create"),
    path('busview', views.bus_view, name="bus_view"),
    path('createroutes', views.create_route, name="create_route"),
    path('directions', views.directions, name="directions"),
    path('settings', views.settings_view, name="settingsview"),
    path('emergency', views.emergency_view, name="emergencyview"),
    path('updatebus/<str:pk>/', views.updatebus, name="updatebus"),
]
