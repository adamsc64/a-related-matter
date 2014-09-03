from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from blog import views


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', views.blog_list, name="blog_list"),
    url(r'^blog/(?P<blog_id>[0-9]+)$', views.blog_detail, name="blog_detail"),
)

# Serve debug toolbar.
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),  # NOQA
    )
