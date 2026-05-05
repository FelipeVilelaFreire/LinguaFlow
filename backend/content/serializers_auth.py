from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name"]


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True, min_length=6)

    def validate_username(self, value: str) -> str:
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate_password(self, value: str) -> str:
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("Password must contain an uppercase letter.")
        if not any(char.islower() for char in value):
            raise serializers.ValidationError("Password must contain a lowercase letter.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain a number.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs["username"], password=attrs["password"])
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        attrs["user"] = user
        return attrs
