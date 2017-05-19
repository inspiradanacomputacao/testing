# coding: utf-8

from django.conf.urls import url, include
from rest_framework import routers
from museuacervo.views import DadosPessoaisViewSet
#PortfolioListView, PortfolioView,

router = routers.DefaultRouter()
router.register(r'dadospessoais', DadosPessoaisViewSet)
#router.register(r'groups', views.GroupViewSet)

urlpatterns = router.urls

'''
helper_patterns = [
    url(r'^portfolios/$', PortfolioListView.as_view(), name='portfolios'),
    url(r'^portfolios/(?P<pk>[0-9]+)/$', PortfolioView.as_view(), name='get_portfolio')

]
'''
#urlpatterns = helper_patterns




'''
from django.conf.urls import url
from museuacervo.views import PortfolioListView, PortfolioView


helper_patterns = [
    url(r'^portfolios/$', PortfolioListView.as_view(), name='portfolios'),
    url(r'^portfolios/(?P<pk>[0-9]+)/$', PortfolioView.as_view(), name='get_portfolio')

]

urlpatterns = helper_patterns

'''



'''
from django.conf.urls import url
from rest_framework import routers
from museuacervo.views import PortfolioListView, PortfolioView



router = routers.DefaultRouter()
router.register(r'portfolio', PortfolioListView)

urlpatterns = router.urls


helper_patterns = [
     url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^museuacervo/$', PortfolioListView.as_view(), name='museuacervo'),
    url(r'^museuacervo/(?P<pk>[0-9]+)/$', PortfolioView.as_view(), name='get_museuacervo'),

]

urlpatterns = helper_patterns
'''