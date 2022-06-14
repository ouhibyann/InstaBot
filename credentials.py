import os

# login credentials as var env
# Here is a ressource to config credentials as .env var -> https://dev.to/biplov/handling-passwords-and-secret-keys-using-environment-variables-2ei0
INSTA_USERNAME = os.environ.get('insta_username')
ISNSTA_PASSWORD = os.environ.get('insta_password')