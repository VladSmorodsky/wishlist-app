from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView

from wishlist_app.api.serializers import WishSerializer, WishDetailSerializer
from wishlist_app.models import Wish


class WishListCreateAPIView(ListCreateAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        """
        Get authenticated user's wishlist
        :return:
        """
        user = self.request.user
        queryset = super().get_queryset()
        return queryset.filter(user=user)


class UserWishListAPIView(ListAPIView):
    queryset = Wish.wishlist.all()
    serializer_class = WishSerializer

    def get_queryset(self):
        """
        Get authenticated user's wishlist
        :return:
        """
        user = self.request.user
        queryset = super().get_queryset()
        return queryset.filter(user=user)


class WishDetailAPIView(RetrieveAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishDetailSerializer
