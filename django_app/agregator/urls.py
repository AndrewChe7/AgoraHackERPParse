from rest_framework import routers
from .views import MainView

main_router = routers.DefaultRouter()
main_router.register(r'', MainView)
urlpatterns = []

urlpatterns += main_router.urls

