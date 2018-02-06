from config import get_client
from birdy.twitter import UserClient

# Use the client to generate the auth token and auth secret
client = UserClient(CONSUMER_KEY, CONSUMER_SECRET)
token = client.get_authorize_token()
AUTH_TOKEN = token.oauth_token
AUTH_TOKEN_SECRET = token.oauth_token_secret

# Prompt the user to visit the auth URL
print "Go to the following URL to get the PIN: "
print token.auth_url

# Get PIN (OAUTH_VERIFIER) from user
OAUTH_VERIFIER = raw_input("Enter PIN: ")

# Use the client to generate the access token and access secret
client = UserClient(CONSUMER_KEY, CONSUMER_SECRET, AUTH_TOKEN, AUTH_TOKEN_SECRET)
token = client.get_access_token(OAUTH_VERIFIER)

# Display OAUTH token and secret
print "Save these values in your application's config.py file: "
print "OAUTH_TOKEN = '" + token.oauth_token + "'"
print "OAUTH_TOKEN_SECRET = '" + token.oauth_token_secret + "'"