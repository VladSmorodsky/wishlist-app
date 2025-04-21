from rest_framework import serializers

from wishlist_app.models import Wish


class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = ['id', 'name', 'description', 'url', 'user']


class WishDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = '__all__'
