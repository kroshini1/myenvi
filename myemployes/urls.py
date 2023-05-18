from django.urls import path

from . import views




urlpatterns = [
    path('', views.index, name="index"),
    path('emplo/',views.emp_details,name="emp")
]
