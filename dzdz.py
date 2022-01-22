import tweepy
api_key ="api_key"
api_secret_key ="api_secret_key"
access_token ="access_token"
secret_access_token = "secret_access_token"
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, secret_access_token)
api = tweepy. API(auth)
try:
    api. verify_credentials ()
    print("Everything works")
except:
    print("Something went wrong")
api.update_status("ur rar xd")
