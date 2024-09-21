from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from blog import views


admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog_list, name="blog_list"),
    re_path(r'^blog/(?P<blog_id>[0-9]+)/$', views.blog_detail, name="blog_detail"),
]

# Serve debug toolbar.
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),  # NOQA
    ]
