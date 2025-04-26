from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, GenericAPIView

from wishlist_app.api.serializers import WishSerializer, WishDetailSerializer
from wishlist_app.models import Wish


class ActiveWishListMixin(GenericAPIView):
    def get_queryset(self) -> QuerySet:
        """
        Get authenticated user's wishlist queryset.
        :return:
        """
        user = self.request.user
        queryset = super().get_queryset()
        return queryset.filter(user=user)


class WishListCreateAPIView(ListCreateAPIView, ActiveWishListMixin):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer


class UserWishListAPIView(ListAPIView, ActiveWishListMixin):
    queryset = Wish.wishlist.all()
    serializer_class = WishSerializer


class WishDetailAPIView(RetrieveAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishDetailSerializer
