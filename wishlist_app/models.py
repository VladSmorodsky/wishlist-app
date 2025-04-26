from django.db import models

from accounts.models import User


class ActiveWishListManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        """
        Get queryset for user's active wishes.
        :return:
        """
        return super().get_queryset().filter(is_active=True)


# Create your models here.
class Wish(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='wish_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    wishlist = ActiveWishListManager()

    def __str__(self):
        return self.name
