from django.shortcuts import render
# to make use of the Article model, it must be imported
from .models import Article
# library for sending simple HTTP responses
from django.http import HttpResponse

# Create your views here.

# view for list of all articles
def article_list(request):
    # grabbing all record of Article database table, ordering by the date field
    articles= Article.objects.all().order_by('date')
    # returning render of a template (Django knows to look in templates folder)
    # parameters for render function are 1. the request object,  2. the template name with relative path from templates directory, and 3. dictionary of data to send to the template (called context)
    return render(request=request, template_name='articles/article_list.html', context={'articles': articles})

# view for a single article with all of its details
# takes in request as first srgument and a slug as the second
def article_detail(request, slug):
    return HttpResponse(slug)
