from django.shortcuts import render, redirect
# to make use of the Article model, it must be imported
from .models import Article
# library for sending simple HTTP responses
from django.http import HttpResponse
# decorator for denoting views for which login is required
from django.contrib.auth.decorators import login_required
# importing our forms
from . import forms

# Create your views here.

# view for list of all articles
def article_list(request):
    # grabbing all record of Article database table, ordering by the date field
    articles= Article.objects.all().order_by('date')
    # returning render of a template (Django knows to look in templates folder)
    # parameters for render function are 1. the request object,  2. the template name with relative path from templates directory, and 3. dictionary of data to send to the template (called context)
    return render(request=request, template_name='articles/article_list.html', context={'articles': articles})

# view for a single article with all of its details
# takes in request as first argument and a slug as the second
def article_detail(request, slug):
    # return HttpResponse(slug)
    # want to query the database for an article based on the provided slug
    # we will then use that aricle's information to fill in a template to be returned by this view
    article= Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

# require login and redirect to login page if not logged in
@login_required(login_url='accounts:login')
def article_create(request):
    if request.method == 'POST':
        # files come along on their own FILES field
        # binding data to forms
        form= forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # want to save article to db
            return redirect(to= 'articles:list')
    else:
        form= forms.CreateArticle()

    return render(request= request, template_name= 'articles/article_create.html', context= {'form': form})
