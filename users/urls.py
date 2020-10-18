"""Define padrões de URL para users"""

from django.conf.urls import url

from django.contrib.auth.views import login

from . import views

urlpatterns = [
    #Página de login
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),

]