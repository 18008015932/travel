from django.conf.urls import url
from user import views


urlpatterns =[
    url(r'home/', views.home),
    url(r'about/', views.about),
    url(r'article/', views.article),
    url(r'detail/', views.detail),
    url(r'resource/', views.resource),

]