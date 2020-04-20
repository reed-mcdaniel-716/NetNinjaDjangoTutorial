"""djangonautic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
# importing Views that'll be referenced from views.py
from . import views

# want to namespace our urls so that the names given to them here can be repeated in other apps without confusion when we need to use them in templates

app_name = 'accounts'

urlpatterns = [
    # parameters are 1. the route string,  2. the view handling the route, and 3. the name for the given URL
    # pre-appended with /accounts/ in base app urls.py
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout")
]
