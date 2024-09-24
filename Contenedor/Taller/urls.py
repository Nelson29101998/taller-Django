
from django.contrib import admin
from django.urls import path, include
from App1.views import IndexView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("App1.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
