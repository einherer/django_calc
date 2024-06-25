from django.urls import path
from calculator.api import api
from django.contrib.auth import views as auth_views
from calculator.views import home, calculator, history

urlpatterns = [
    path("api/", api.urls),
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('calculator/', calculator, name='calculator'),
    path('history/', history, name='history'),
]