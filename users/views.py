
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """Faz logout do usuário."""
    logout(request)
    # return HttpResponseRedirect(reverse('learning_logs:index'))
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
	"""Faz o cadastro de um novo usuário."""
	if request.method != 'POST':
		# Exibe o formulário de cadastro em branco
		form = UserCreationForm()
	else:
		# Processa o formulário preenchido
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			# Faz login do usuario e o redireciona para a pagina inicial
			authenticate_user = authenticate(username=new_user.username,password=request.POST['password1'])
			login(request, authenticate_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))
	context = {'form': form}
	return render(request, 'users/register.html', context)

    



