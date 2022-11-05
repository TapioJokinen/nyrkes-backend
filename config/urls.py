from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from menel.api.views.token import CookieTokenObtainPairView, CookieTokenRefreshView

urlpatterns = [
    path("auth/token/", CookieTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", CookieTokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include("menel.api.urls")),
]

if settings.DEBUG:
    dev_urlpatterns = [
        path("admin/", admin.site.urls),
    ] + urlpatterns
