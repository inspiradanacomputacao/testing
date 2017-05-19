from django.conf.urls import url

from . import views
   
urlpatterns = [
    # filme views
    url(r'^$', views.filme_list, name='filme_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
           r'(?P<filme>[-\w]+)/$',
           views.filme_detail,
           name='filme_detail'),
]