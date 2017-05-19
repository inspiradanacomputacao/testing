from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.museuacervo_exibir),
]