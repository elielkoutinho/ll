from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import TopicForm, EntryForm

from .models import Topic
from .forms import TopicForm

def index(request):
    """A página inicial de Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra todos os assuntos."""
    topics = Topic.objects.order_by('date_added')                       #w
    context = {'topics': topics}                                        #X
    return render(request, 'learning_logs/topics.html', context)        #Y 


def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added') # O sinal "-" antes de date ordena os resultados em ordem inversa
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Adiciona um novo assunto."""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = TopicForm
    else:
        # Dados de POST submetidos; processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
    

def new_entry(request, topic_id):
    """Acrescenta uma nova entrada para um assunto em particular."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = EntryForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}        
    return render(request, 'learning_logs/new_entry.html', context)













