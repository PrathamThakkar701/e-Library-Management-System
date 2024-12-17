from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', home),
    path('save', save_student),
    path('logout', views.logout_view),
]