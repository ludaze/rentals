from rest_framework import serializers
from api.models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username','email', 'phone_number','verification_document', 'is_verified']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['full_name'] = user.profile.full_name
        token['user_name'] = user.username
        token['email '] = user.email
        token['verification_document'] = user.profile.verification_document
        token['is_verified'] = user.profile.is_verified

        return token
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password] )

    class Meta:
        model = CustomUser
        fields = ['email', 'username','password']

    def create(self,validated_data):
        user = CustomUser.objects.create(
            username = validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user