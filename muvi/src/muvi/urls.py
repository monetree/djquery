
from django.conf.urls import url
from django.contrib import admin
from api.views import usergeneratedcontent,ajax

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', usergeneratedcontent),
    url(r'^ajax$', ajax),
]
