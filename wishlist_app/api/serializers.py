from rest_framework import serializers

from wishlist_app.models import Wish


class WishSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Wish
        fields = ['id', 'name', 'description', 'url', 'user', 'image']


class WishDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = '__all__'
