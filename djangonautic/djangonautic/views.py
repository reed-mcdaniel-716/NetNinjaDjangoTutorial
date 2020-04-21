# funtions for handling various url routes
# When a page is requested, Django creates an HttpRequest object that contains metadata about the request
    # Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function
    # Each view is responsible for returning an HttpResponse object
# library for sending simple HTTP responses
from django.http import HttpResponse
#library for rendering templates
from django.shortcuts import render

# every View function takes an HttpRequest as an argument
# and returns a HttpResponse
'''def homepage(request):
    # plain text response
    # return HttpResponse('homepage')
    # returning render of a template (Django knows to look in templates folder)
    # parameters for render function are 1. the request object and 2. the template name
    return render(request, 'homepage.html')'''


def about(request):
    # plain text response
    # return HttpResponse('about')
    # returning render of a template
    return render(request, 'about.html')
