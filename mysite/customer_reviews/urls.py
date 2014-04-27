from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<supplier_slug>[a-zA-Z0-9\-]+)/$', views.supplier_reviews, name='supplier_reviews'),
    url(r'^(?P<supplier_slug>[a-zA-Z0-9\-]+)/write/$', views.supplier_review_create, name='supplier_review_create'),
)
