from django.conf.urls import url
from RestMongo import views

urlpatterns =[
    url(r'^api/tutorials$',views.tutorial_list,name="list"),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$',views.tutorial_detail),
    url(r'^api/tutorials/published$',views.tutorial_list_published,name="published")
    
]