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

app_name = 'articles'
# Remember: Django runs through urls in order until it hits a match, so you want the most general route i.e. the '' route for the homepage, to be last
urlpatterns = [
    # parameters are 1. the route string,  2. the view handling the route, and 3. the name for the given URL
    # will be pre-appended with articles/ based on specification in root app's urls.py (see djangonautic/urls.py)
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    path('<slug:slug>/', views.article_detail, name="detail")
]
