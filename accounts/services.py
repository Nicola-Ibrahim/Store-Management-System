import jwt
import datetime
from django.conf import settings


def create_token(user_id):
    payload = dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(24),
        iat=datetime.datetime.utcnow(),
    )
    print(payload)

    token = jwt.encode(payload=payload, key=settings.JWT_PRIVATE_KEY, algorithm='HS256')
    return token