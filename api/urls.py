from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('movies', views.MovieViewSet)
router.register('ratings', views.RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
