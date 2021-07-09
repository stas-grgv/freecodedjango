from django.http import HttpResponse as hr
from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here.
from pages.forms import RegisterForm


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "title": "this is about me",
        "my_number": 123,
        "my_list": [123, 42, 24, 'bce']
    }
    return render(request, "about.html", my_context)


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
