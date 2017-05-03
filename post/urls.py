from rest_framework import routers
from .views import PostViewSet, CommentViewSet, UserViewSet


router = routers.SimpleRouter()
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)
router.register("users", UserViewSet)

urlpatterns = router.urls
