from django.contrib.auth.models import AnonymousUser
from django.conf import settings
from django.contrib.auth.middleware import get_user
import jwt

from django_react_store import settings
from main_app.models import Customer


def jwt_auth_middleware(get_response):
    """Sets the user object from a JWT header"""

    def middleware(request):
        user_jwt = get_user(request)
        if user_jwt.is_authenticated:
            return user_jwt
        token = request.META.get('HTTP_AUTHORIZATION', None)

        if token is not None:
            try:
                user_jwt = jwt.decode(
                    token,
                    settings.SECRET_KEY,
                    algorithms=['HS256']
                )
                request.user = Customer.objects.get(
                    id=user_jwt['user_id']
                )
            except Exception as e:
                request.user = AnonymousUser

        response = get_response(request)

        return response

    return middleware
