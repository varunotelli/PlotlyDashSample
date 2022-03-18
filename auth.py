import pyrebase

config = {
	'apiKey': "AIzaSyCcRkC2f-MzBXr4OYr5v-FzCgIv43xQ9Bc",
	'authDomain': "temp-2060c.firebaseapp.com",
	'databaseURL': "https://temp-2060c-default-rtdb.firebaseio.com",
	'projectId': "temp-2060c",
	'storageBucket': "temp-2060c.appspot.com",
	'messagingSenderId': "212543260481",
	'appId': "1:212543260481:web:b97fe49d25e22d75bfc3c0",
	'measurementId': "G-W56EWCR0JD"
	};

firebase = pyrebase.initialize_app(config)
fb_auth = firebase.auth()

def login(username, password):
	
	try:
		user = fb_auth.sign_in_with_email_and_password(username, password)
		return user
	except:
		return None

def create_account(username, password):
	try:
		user = fb_auth.create_user_with_email_and_password(username, password)
		return user
	except:
		return None