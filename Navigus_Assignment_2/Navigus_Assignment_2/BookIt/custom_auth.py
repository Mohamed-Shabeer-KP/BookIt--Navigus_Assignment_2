from django.contrib.auth.models import User

class EmailAuthBackend(object):
	"""
	Allows a user to sign in using an email/password pair rather than
	a username/password pair.
	"""
 
def authenticate(mail=None, password=None):
    try:
        user = User.objects.get(email=mail)
        if user.check_password(password):
            return user
    except User.DoesNotExist:
        return None
 
def get_user(user_id):
    try:
        return User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return None
