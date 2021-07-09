from django.urls import path
from pages import views

app_name = 'pages'
urlpatterns = [
    path('', views.home_view, name='homepage'),
    path('contact', views.contact_view, name='contact page'),
    path('about', views.about_view, name='about page'),
    path('register', views.registration_view, name='register'),
]
