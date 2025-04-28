import re

from rest_framework import serializers

from accounts.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def validate_password(self, value) -> str:
        """
        Validate secure password
        :param value:
        :return:
        """
        if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*[@#$%&_]).{8,}$', value) is None:
            raise serializers.ValidationError('Password must contain symbols: a-z, A-Z, 0-9, @#$%&_')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords must match')
        return data

    def create(self, validated_data) -> User:
        user = User.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
