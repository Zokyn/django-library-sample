from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='catalog/')),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
