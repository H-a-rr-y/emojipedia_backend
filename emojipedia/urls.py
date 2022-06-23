from django.urls import *
from rest_framework.routers import *

from .views import *

router = DefaultRouter()
router.register("emoji", EmojiViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]