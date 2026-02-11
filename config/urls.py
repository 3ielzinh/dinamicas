"""
URL Configuration for +100 Dinâmicas Para Retiro na Igreja.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Authentication (Django Allauth)
    path('accounts/', include('allauth.urls')),
    
    # Local apps
    path('', include('apps.core.urls')),
    path('dinamicas/', include('apps.dinamicas.urls')),
    path('perfil/', include('apps.accounts.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Customize admin site
admin.site.site_header = "+100 Dinâmicas Para Retiro"
admin.site.site_title = "Administração"
admin.site.index_title = "Gerenciamento de Dinâmicas"
