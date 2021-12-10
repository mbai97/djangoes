from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from user import views
# from django.conf import settings
#\ from django.conf.urls.static import static
# from django.urls.resolvers import URLPattern

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('user.urls')),
    # path('', views.home, name='home'),
]

# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)