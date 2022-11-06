from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from menel.api.views.token import (
    CookieTokenBlacklistView,
    CookieTokenObtainPairView,
    CookieTokenRefreshView,
    CookieTokenVerifyView,
)

urlpatterns = [
    path("auth/token/", CookieTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", CookieTokenRefreshView.as_view(), name="token_refresh"),
    path("auth/token/blacklist/", CookieTokenBlacklistView.as_view(), name="token_blacklist"),
    path("auth/token/verify/", CookieTokenVerifyView.as_view(), name="token_verify"),
    path("api/", include("menel.api.urls")),
]

if settings.DEBUG:
    dev_urlpatterns = [
        path("admin/", admin.site.urls),
    ] + urlpatterns
