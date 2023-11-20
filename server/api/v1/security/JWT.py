from fastapi_users.authentication import JWTStrategy

from server.settings import Auth


def get_jwt() -> JWTStrategy:
    return JWTStrategy(secret=Auth.SECRET, lifetime_seconds=Auth.jwt_age)
