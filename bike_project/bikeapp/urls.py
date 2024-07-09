# bikeapp/urls.py

from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import BikeViewSet, RiderViewSet, BikeAllotmentViewSet, PaymentViewSet , bike_list ,index

router = DefaultRouter()
router.register(r'bikes', BikeViewSet)
router.register(r'riders', RiderViewSet)
router.register(r'bikeallotments', BikeAllotmentViewSet)
router.register(r'payments', PaymentViewSet)

# urlpatterns = [
#    path('admin/', admin.site.urls),
#     path('', include('bikeapp.urls')),
# ]

# bikeapp/urls.py

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BikeViewSet, RiderViewSet, BikeAllotmentViewSet, PaymentViewSet, index, bike_list

# router = DefaultRouter()
# router.register(r'bikes', BikeViewSet)
# router.register(r'riders', RiderViewSet)
# router.register(r'bikeallotments', BikeAllotmentViewSet)
# router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('bikes/', bike_list, name='bikes-list'),
    path('api/', include(router.urls)),
]

