from django.urls import path
from pages import views
from django.contrib.auth import views as auth_views

app_name = 'pages'
urlpatterns = [
    path('', views.home_view, name='homepage'),
    path('contact', views.contact_view, name='contact page'),
    path('about', views.about_view, name='about page'),
    path('register', views.registration_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout')
]
