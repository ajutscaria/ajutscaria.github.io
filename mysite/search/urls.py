from django.conf.urls import url

from search import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_destination/$', views.add_destination, name='add_destination'),
    url(r'^search_for_location/$', views.search_for_location, name='search_for_location'),
    url(r'^add_point_of_interest/$', views.add_point_of_interest, name='add_point_of_interest'),
]