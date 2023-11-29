from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('menu.urls')),
    path('admin/', admin.site.urls),
    path('cadastro/', include('cadastro.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('treino/', include('treino.urls')),
    path('exercicios/', include('exercicios.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#If not in deployment
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)