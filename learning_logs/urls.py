"""Define padrões de URL para learning_logs."""

from django.conf.urls import url

from .import views

urlpatterns = [ 
        # Página inicial
        url(r'^$', views.index, name='index'),

        # Mostra todos os assuntos
        url(r'^topics/$', views.topics, name='topics'),

        # Página de detalhes para um único assunto
        url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

        # Página para adicionar um novo assunto
        url(r'^new_topic/$', views.new_topic, name='new_topic'),

        # Página para adicionar uma nova entrada
        url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry,name='new_entry'),

        # Página para editar uma entrada        
        url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
        
]