from products.models import Order
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from pages.forms import RegisterForm, LoginForm


def home_view(request, *args, **kwargs):
    user = request.user
    try:
        orders = Order.objects.get(client_user=user)
    except:
        orders = "no orders"
    context = {
        "username": user.username,
        "orders": orders,
    }

    return render(request, "home.html", context)


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "title": "this is about me",
        "my_number": 123,
        "my_list": [123, 42, 24, 'bce']
    }
    return render(request, "about.html", my_context)


def login_view(request, *args, **kwargs):
    loginForm = LoginForm(request.POST)
    if request.method == 'POST':
        context = {
            "form": loginForm,
        }
        if loginForm.is_valid():
            cd = loginForm.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect("/")
    else:
        context = {
            "form": loginForm,
        }
        form = LoginForm()

    return render(request, "login.html", context)


# TODO: Set logout function
def logout_view(request):
    logout(request)
    return redirect('/')


def registration_view(request, *args, **kwargs):
    my_form = RegisterForm(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form = RegisterForm()
        return redirect('/')
    context = {
        "register_form": my_form,
    }
    return render(request, "registration-form.html", context)
