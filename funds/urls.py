from django.urls import include, path
from rest_framework import routers
from . import views
from .views import get_id

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'CompaniesName',views.CpViewSet)
router.register(r'Mutualfunds',views.MfViewSet)
router.register(r'Matchingfield',views.MatchingViewSet)
router.register(r'JoinTableModel',views.JoinTableApi)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('JoinTableModelbyId/<id>/',get_id),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]