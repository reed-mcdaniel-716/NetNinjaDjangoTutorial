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
from django.contrib import admin
from django.urls import path
# use include to add urls from other applications
from django.urls import include
# importing Views that'll be referenced from views.py
from . import views
# for working with static files in local development, NEVER PRODUCTION!
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Remember: Django runs through urls in order until it hits a match, so you want the most general route i.e. the '' route for the homepage, to be last
urlpatterns = [
    path('admin/', admin.site.urls),
    # parameters are 1. the route string and 2. the view handling the route
    path('about/', views.about),
    # '' for the homepage
    path('', views.homepage),
    # any urls defined in articles app will be pre-appended with articles/
    path('articles/', include('articles.urls'))
]

# function will first check to see that we are in debug mode (should only be true in development) then append itself
urlpatterns += staticfiles_urlpatterns()
