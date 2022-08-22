from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "Welcome_page"),
    path('unit/', views.viewUnit, name = "Unit_page"),
    path('unit/<int:unit_id>', views.viewDetails, name = "Ques_page"),
]