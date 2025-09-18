from AnLuckBackend import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('User.urls')),
    path('', include('User.auth.urls')),
    path('', include('Posts.urls')),
    path('', include('Likes.urls')),
    path('', include('Comments.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)