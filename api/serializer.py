from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists, get_username_max_length
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers

from obis_registration.models import InviteUser

class UserSerializer(serializers.Serializer):
    username   = serializers.CharField(max_length=100)
    email      = serializers.EmailField()
    first_name = serializers.CharField(max_length=50)
    last_name  = serializers.CharField(max_length=50)

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password1 = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)

    # def username_exists(username, exclude_user=None):
    #     from django.contrib.auth import get_user_model
    #     from django.contrib.auth.models import User

    #     users = User.objects
    #     if exclude_user:
    #         users = users.exclude(user=exclude_user)
    #     ret = users.filter(username__iexact=username).exists()
    #     if not ret:
    #         user_field = allauth_settings.USER_MODEL_USERNAME_FIELD
    #         if user_field:
    #             users = get_user_model().objects
    #             if exclude_user:
    #                 users = users.exclude(pk=exclude_user.pk)
    #             ret = users.filter(**{user_field + "__iexact": username}).exists()
    #     return ret
    
    # def validate_username(self, username):
    #     username = get_adapter().clean_username(username)
    #     if username and self.username_exists(username):
    #         raise serializers.ValidationError(
    #             ("This username already exists."))
    #     return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    ("A user is already registered with this e-mail address."))
        return email
    
    def validate_password1(self, password):
        return get_adapter().clean_password(password)
    
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                ("The two password fields didn't match."))
        return data
    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        InviteUser.objects.filter(email__exact=user.email).delete()
        return user
