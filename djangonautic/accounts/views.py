from django.shortcuts import render, redirect
# importing user creation and login authentication forms provided by Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# importing the login and logout functions
from django.contrib.auth import login, logout
# Create your views here.

def signup_view(request):
    # UserCreationForm has three fields:
        # 1. username (from the user model)
        # 2. password1
        # 3. password2
    # It verifies that password1 and password2 match, validates the password using validate_password(), and sets the user’s password using set_password()

    # this View will be recieveing both GET and POST requests
        # we are used to recieveing GET requests, for which we return some type of HTML template
        # for a POST request, we will process the submitted data

    # handling request if its a POST reques
    if request.method == 'POST':
        # request.POST contains the post data
        # doing this validates our input, returning a form which is eith valid or invalid
        form = UserCreationForm(data= request.POST)
        if form.is_valid():
            # saving user to database and returns user
            user= form.save()
            # log user in
            login(request, user)
            # redirect user to article list
            return redirect(to='articles:list')
    # handling request if its a GET request
    else:
        # instance of the user creation form
        form = UserCreationForm()

    # outside of if else because it handles any type of request that isn't a POST request, including GET request, and forms that were posted but invalid (will see helpers)
    return render(request= request, template_name= 'accounts/signup.html', context= {'form': form})
def login_view(request):
    # handle both POST and GET methods
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            # log user in
            user= form.get_user()
            login(request, user)
            # checking to see if 'next' is defined for specified redirect
            if 'next' in request.POST:
                # redirect to URL specified as 'next'
                return redirect(to= request.POST.get('next'))
            else:
                # redirect user to article list
                return redirect(to= 'articles:list')
    else:
        form = AuthenticationForm()

    # default return
    return render(request= request, template_name= 'accounts/login.html', context= {'form':form})

def logout_view(request):
    # best practice is to process a post request as a result of a button click or other interation to log a user out
    if request.method == 'POST':
        logout(request)
        return redirect(to='articles:list')
