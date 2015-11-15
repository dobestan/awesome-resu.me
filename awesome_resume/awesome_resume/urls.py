from django.conf.urls import include, url
from django.contrib import admin

from multisites.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', HomeView.as_view(), name='home'),
]
