from rest_framework import routers

from .api.api import MenuCardViewSet, DishViewSet

router = routers.SimpleRouter()
router.register('menu-cards', MenuCardViewSet, 'menu-cards')
router.register('dishes', DishViewSet, 'dishes')


urlpatterns = router.urls
