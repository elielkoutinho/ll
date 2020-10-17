from django.shortcuts import render

from .models import Topic

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





