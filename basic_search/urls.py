from django.conf.urls import url

from basic_search import views

urlpatterns = [
    url(r'^searchform/$', views.search_form),
    url(r'^search/$', views.search, name='search'),
]