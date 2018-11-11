from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.render_main_page, name='main'),
    url(r'^visualize/(?P<temp>[-+]?\d*\.\d+|\d+)/$', views.render_visualize_page, name='visualize'),
]
