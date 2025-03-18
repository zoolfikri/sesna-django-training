"""
URL configuration for sesna project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import LogoutView, PingView, BooksView, TokenObtainPairView


schema_view = get_schema_view(
    openapi.Info(
        title="Sesna API",
        default_version='v1',
        description="API documentation for Sesna project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@sesna.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-token', TokenObtainPairView.as_view(), name='get-token'),
    path("logout", LogoutView.as_view(), name="logout"),
    path('sesna/ping', PingView.as_view(), name='ping'),
    path('sesna/books', BooksView.as_view(), name='books'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
