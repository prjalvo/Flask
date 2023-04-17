from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings # new
from  django.conf.urls.static import static #new

schema_view = get_schema_view(
    openapi.Info(
        title="Backend Online Shop APIS",
        default_version='1.0.0',
        description="This is swagger for our apis."

    ),
    public=True,
)

urlpatterns = [
      
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
