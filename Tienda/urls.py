from rest_framework import routers
from .views import UbicacionListView, CategoriaListView, UsuarioListView, RopaListView, FacturaListView, CarritoListView

router = routers.DefaultRouter()
router.register('api/ubicacion', UbicacionListView, basename='ubicacion')
router.register('api/categoria', CategoriaListView, basename='categoria')
router.register('api/usuario', UsuarioListView, basename='usuario')
router.register('api/ropa', RopaListView, basename='ropa')
router.register('api/factura', FacturaListView, basename='factura')
router.register('api/carrito', CarritoListView, basename='carrito')

urlpatterns = router.urls
