from django.urls.conf import path

from . import views

urlpatterns = [
    path('wishes/', views.WishListCreateAPIView.as_view(), name='wish_list'),
    path('wishes/<int:pk>/', views.WishDetailAPIView.as_view(), name='wish_detail'),
    path('user-wishes/', views.UserWishListAPIView.as_view(), name='user_wish_list')
]
