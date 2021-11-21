from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='core:index'), name='logout'),
    path('home/', views.home, name='home'),
]