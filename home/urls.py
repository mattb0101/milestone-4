from django.urls import path
# this imports views/py from current directory
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('email/', views.email, name='email'),
]
