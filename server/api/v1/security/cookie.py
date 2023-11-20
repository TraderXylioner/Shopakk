from fastapi_users.authentication import CookieTransport

from server.settings import Auth

cookie_transport = CookieTransport(cookie_name='Auth', cookie_max_age=Auth.cookie_age)
