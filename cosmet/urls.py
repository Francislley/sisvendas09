from django.conf.urls import url
from django.contrib import admin
from cosmet.core.views import home, login, gerencia

urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^gerencia/', gerencia, name='gerencia'),
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
]
