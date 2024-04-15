from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'sources', views.SourceViewSet)
router.register(r'source-types', views.SourceTypeViewSet)
# router.register(r'update-source', views.update_sources)

urlpatterns = router.urls

urlpatterns.append(path('update-source/', views.update_sources))
urlpatterns.append(path('update-articles/', views.make_update_articles))
urlpatterns.append(path('update-cache/', views.delete_cache_dupes))
