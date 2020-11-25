from django.conf.urls import include, url

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/doc/', include(django.contrib.admindocs.urls)),


    ]
