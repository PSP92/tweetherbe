from rest_framework import routers, viewsets
from . import views
# from uploadviews import UploadView

router = routers.DefaultRouter()
router.register(r"user", views.UserViewSet)
router.register(r"tweets", views.TweetsViewSet)

urlpatterns = router.urls
