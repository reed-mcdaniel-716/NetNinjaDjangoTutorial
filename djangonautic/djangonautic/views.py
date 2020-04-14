# funtions for handling various url routes
# When a page is requested, Django creates an HttpRequest object that contains metadata about the request
    # Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function
    # Each view is responsible for returning an HttpResponse object
# library for sending simple HTTP responses
from django.http import HttpResponse

# every View function takes an HttpRequest as an argument
def homepage(request):
    # plain text response
    return HttpResponse('homepage')
    
def about(request):
    # plain text response
    return HttpResponse('about')
