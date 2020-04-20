from django.shortcuts import render

# Create your views here.

def signup_view(request):
    # parameters for render function are 1. the request object,  2. the template name with relative path from templates directory, and 3. dictionary of data to send to the template (called context)
    return render(request, 'accounts/signup.html')
