from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = []

if settings.DEBUG:
    dev_urlpatterns = [
        path("admin/", admin.site.urls),
    ] + urlpatterns
