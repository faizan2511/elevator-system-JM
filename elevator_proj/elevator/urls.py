from django.urls import path
from . import views

urlpatterns = [
    path('get-direction/<int:id>', views.get_direction),
    path('get-next-destination/', views.get_next_destination),
    path('open-door/', views.open_door),
    path('close-door', views.close_door)
    
]