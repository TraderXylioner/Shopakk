from fastapi_users.authentication import AuthenticationBackend

from server.api.v1.security.cookie import cookie_transport
from server.api.v1.security.JWT import get_jwt

auth = AuthenticationBackend(name='jwt', transport=cookie_transport, get_strategy=get_jwt)
