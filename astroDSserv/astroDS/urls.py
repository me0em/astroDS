
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('main.urls')),
    url(r'^admin/', admin.site.urls),
]
