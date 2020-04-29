from rest_framework import routers

from .viewset import *




router = routers.SimpleRouter()
router.register('appdjango', VendedorViewset)

urlpatterns = router.urls




router = routers.SimpleRouter()
router.register('appdjango', CompradorViewset)

urlpatterns = router.urls


router = routers.SimpleRouter()
router.register('appdjango', ArticuloViewset)

urlpatterns = router.urls




router = routers.SimpleRouter()
router.register('appdjango', EnvioViewset)

urlpatterns = router.urls


router = routers.SimpleRouter()
router.register('appdjango', RegistroViewset)

urlpatterns = router.urls
