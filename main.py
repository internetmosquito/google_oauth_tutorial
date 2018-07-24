import webapp2
from webapp2 import Route
from webapp2_extras import sessions

from OAuthHandler import OAuthHandler, AuthorizeHandler, CallbackHandler, OAuthTokenHandler

# Session Configurations
configuration = {}
configuration['webapp2_extras.sessions'] = {
   'secret_key': "secret_session_key",
}

# Routes
application = webapp2.WSGIApplication([
   Route('/', handler=OAuthHandler, name='oauth'),
   Route('/oauth', handler=OAuthHandler, name='oauth'),
   Route('/oauth/', handler=OAuthHandler, name='oauth'),
   Route('/oauth/authorize', handler=AuthorizeHandler, name='auth'),
   Route('/oauth/callback', handler=CallbackHandler, name='cb'),
   Route('/oauth/token', handler=OAuthTokenHandler, name='oauth-token'),
], debug=True, config=configuration)