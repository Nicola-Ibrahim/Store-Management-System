
from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings
import jwt

from . import models

class CustomAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('jwt')


        if not token:
            return None
            
        try:
            payload = jwt.decode(token, key=settings.JWT_PRIVATE_KEY, algorithms='HS256')
        
        except :
            raise exceptions.AuthenticationFailed("Unauthorized")

        user = models.User.objects.filter(id=payload.get('id')).first()

        return (user, None)


