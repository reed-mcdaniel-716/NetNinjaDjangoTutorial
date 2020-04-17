from django.shortcuts import render

# Create your views here.

def article_list(request):
    # returning render of a template (Django knows to look in templates folder)
    # parameters for render function are 1. the request object and 2. the template name with relative path from templates directory
    return render(request, 'articles/article_list.html')
