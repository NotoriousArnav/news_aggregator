from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'sources', views.SourceViewSet)
router.register(r'source-types', views.SourceTypeViewSet)

urlpatterns = router.urls
