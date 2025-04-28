from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.api.serializers import RegisterSerializer
from celery_tasks.tasks import send_register_email, send_market_email, SEND_MARKET_EMAIL_COUNTDOWN


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    status_code = status.HTTP_201_CREATED
    permission_classes = (AllowAny,)

    def perform_create(self, serializer) -> None:
        user = serializer.save()
        send_register_email.delay(user.email)
        send_market_email.apply_async(args=[user.email], countdown=SEND_MARKET_EMAIL_COUNTDOWN)
        token = RefreshToken.for_user(user)
        self.token = token.access_token

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=self.status_code, data={'access': str(self.token)})
