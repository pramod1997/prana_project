from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [

    url(r'^first$', views.model_form_upload, name='model_form_upload'),
    url(r'^second/\d{1,2}$', views.second, name='second'),
   	url(r'^third$', views.third, name='third'),
   
]