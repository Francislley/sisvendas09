from django.conf.urls import url
from django.contrib import admin
from cosmet.core.views import home, login

urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
]
