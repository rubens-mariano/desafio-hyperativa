from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Card API",
      default_version='v1',
      description="API para cadastro e consulta de número de cartão completo",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ru_bens@outlook.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[AllowAny,],
)


def redirect_redoc(*args, **kwargs):
    return redirect('/redoc/')


urlpatterns = [
    path('', redirect_redoc),
    path('admin/', admin.site.urls),
    path('api/', include('card.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
