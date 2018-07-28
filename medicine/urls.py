from django.conf.urls import url
from . import views

urlpatterns = [
    #/medicine/
    url(r'^$',views.homePage, name='homePage'),
    url(r'^product/$',views.product, name='product'),
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
