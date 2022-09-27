from .views import *

from rest_framework import routers


router = routers.SimpleRouter()

router.register(r'ratings', RatingViewSet)
router.register(r'deal_types', DealTypeViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'inventories', InventoryTypeViewSet)

router.register(r'counterparties', CounterpartyViewSet)
router.register(r'deals', DealViewSet)

urlpatterns = router.urls
