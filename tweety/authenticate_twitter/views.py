from django.shortcuts import render
import tweepy
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
import json
from authenticate.views import RedirectToAuthenticationPage
from authenticate_twitter.models import apitable

api = None
# Create your views here.
def get_authorization_url(request):

        # URL to where we will redirect to
		redirect_url = "http://127.0.0.1:8000/twitter_redirect_url"

        # create the handler
		auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET, redirect_url)

        # get the authorization url (i.e. https://api.twitter.com/oauth/authorize?oauth_token=XXXXXXX)
        # this method automatically grabs the request token first
        # Note: must ensure a callback URL (can be any URL) is defined for the application at dev.twitter.com,
        #       otherwise this will fail (401 Unauthorized)
		url = ""
		try:
			url = auth.get_authorization_url()

		except tweepy.error.TweepError as e:
			print(e)

		print(auth.request_token.keys())
		request.session['twitter_request_token_key'] = auth.request_token['oauth_token']
		request.session['twitter_request_token_secret'] = auth.request_token['oauth_token_secret']

		return HttpResponseRedirect(url)

def verify(request):
	if 'denied' in request.GET:
		return HttpResponse("Authentication failed")

	print(request.session.keys())

	if 'twitter_request_token_key' not in request.session \
		or 'oauth_token' not in request.GET \
		or 'oauth_verifier' not in request.GET \
		or request.session['twitter_request_token_key'] != request.GET['oauth_token']:

		return HttpResponse("Authentication failed")
	else:
		data = {}
		auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
		token  = request.GET['oauth_token']
		verifier = request.GET['oauth_verifier']

		request_token = {
							'oauth_token':token,
							'oauth_token_secret': verifier
						}

		auth.request_token = request_token				

		if 'twitter_access_token_key' not in request.session:
			access_token = auth.get_access_token(request.GET['oauth_verifier'])
			print(access_token)
			request.session['twitter_access_token_key'] = access_token[0]
			request.session['twitter_access_token_secret'] = access_token[1]

		else:
			auth.set_access_token(request.session['twitter_access_token_key'], request.session['twitter_access_token_secret'])

		api = tweepy.API(auth_handler=auth)
		
		user = api.me()

		#insertion into table to get api in commandcenter
		u=apitable.objects.create(screen_name = user.screen_name, twitter_oauth_token=token,twitter_oauth_verifier=verifier,twitter_access_token_key=request.session['twitter_access_token_key'],twitter_access_token_secret=request.session['twitter_access_token_secret'])
		
		

		#print(user.screen_name)
		request.session['twitter_screen_name'] =user.screen_name
		return RedirectToAuthenticationPage(request)