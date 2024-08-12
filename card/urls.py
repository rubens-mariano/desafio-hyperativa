from django.urls import path, include
from .views import CardViewSet, FileUploadView
from rest_framework import routers


def configure_router():
    """ Criação das rotas para acesso as Views """
    router = routers.DefaultRouter()
    router.register('cards', CardViewSet, basename='Cards')
    return router


router = configure_router()
urlpatterns = [
    path('', include(router.urls)),
    path('upload/', FileUploadView.as_view(), name='cards-upload'),
]
