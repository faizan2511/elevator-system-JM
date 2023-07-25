# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('initialize-elevators/', views.initialize_system),
    path('get-requests/', views.get_all_requests),
    path('save-requests/', views.save_user_requests),
    path('mark-in-maintenance/<int:id>', views.mark_elevator_in_maintenance),
]