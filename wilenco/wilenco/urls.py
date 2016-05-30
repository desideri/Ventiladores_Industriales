from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'wilenco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'web.views.index'),
    url(r'^contacto/', 'web.views.contacto'),
    url(r'^productos/', 'web.views.product'),
    url(r'^empresa/', 'web.views.empresa'),
]
