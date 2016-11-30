from django.conf.urls import url
from django.contrib import admin
from cosmet.core.views import home, index
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy

urlpatterns = [

    url(r'^login/$', login, {"template_name": "core/login.html"}, name="login"),
    url(r'^$', index),

    # A view 'django.contrib.auth.views.logout' para /logout/URL.
    # é necessário passar três parâmetros sendo um deles um dicionário
    # informando qual página deve ser chamada após o logout.
    url(r'^logout/$', logout,{"next_page": reverse_lazy('login')}, name="logout"),
    url(r'^accounts/profile/$', home, name="url_home"),
    url(r'^admin/', admin.site.urls),
]
