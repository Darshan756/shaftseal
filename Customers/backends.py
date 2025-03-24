# backends.py
from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except CustomUser.DoesNotExist:
                return None
        else:
            try:
                user = CustomUser.objects.get(phone_no=username)
            except CustomUser.DoesNotExist:
                return None

        if user and user.check_password(password):
            return user

        return None
