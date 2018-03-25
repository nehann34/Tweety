from yellowant import YellowAnt
from django.conf import settings
import json
import itertools
from yellowant.messageformat import MessageClass,MessageAttachmentsClass,AttachmentFieldsClass
from django.http import JsonResponse
import tweepy

class CommandCenter(object):
	def __init__(self,yellowant_user_id,yellowant_integration_id,function_name,args,api):
		self.yellowant_user_id=yellowant_user_id
		self.yellowant_integration_id=yellowant_integration_id
		self.function_name=function_name
		self.args=args
		data = {}
		auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
		token  = api.twitter_oauth_token
		verifier = api.twitter_oauth_verifier

		request_token = {
							'oauth_token':token,
							'oauth_token_secret': verifier
						}

		auth.request_token = request_token				

		

		auth.set_access_token(api.twitter_access_token_key, api.twitter_access_token_secret)
		self.api = tweepy.API(auth_handler=auth)
		user = self.api.me()

		print(user.screen_name)

		

	def parse(self):
		self.commands={
			'dm':self.dm,
			'favourite':self.favourite,
			'follow':self.follow,
			'home':self.home,
			'search':self.search,
			'status':self.status,
			'unfavourite':self.unfavourite,
			'unfollow':self.unfollow,

		}
		return self.commands[self.function_name](self.args)

	def dm(self,args):
		handle=args['handle']
		message=args['message']
		try:
			self.api.send_direct_message(handle,text=message)
		except:
			m  = MessageClass()
			m.message_text="Message can't be sent!!!"
			return m.to_json()
		m=MessageClass()
		m.message_text="You just successfully sent a message to user "+handle
		return m.to_json()

	def favourite(self,args):
		id=args['id']
		try:
			self.api.create_favorite(id)
		except:
			m  = MessageClass()
			m.message_text="Status can't be added to favourites!!!"
			return m.to_json()
		m=MessageClass()
		m.message_text="Status with id=" + id + " is added to favorites!!!"
		return m.to_json()
	
	def follow(self,args):
		handle=args['handle']
		try:
			self.api.create_friendship(handle)
		except:
			m  = MessageClass("person can't be followed")
			m.message_text="!!!"
			return m.to_json()
		m=MessageClass()
		m.message_text="you followed a person with screen_name="+handle
		return m.to_json()

	def home(self,args):
		try:
			l=self.api.home_timeline(count=30)
		except:
			m  = MessageClass()
			m.message_text="can't get the feed!!!"
			return m.to_json()

		m=MessageClass()
		for status in l:
			st=MessageAttachmentsClass()
			st.title=status.author.screen_name+" "+str(status.id)
			tweet=AttachmentFieldsClass()
			tweet.value=status.text
			st.attach_field(tweet)
			m.attach(st)
		return m.to_json()
	
	
	def search(self,args):
		query=args['query']
		try:
			p=self.api.search_users(query)
		except:
			m  = MessageClass()
			m.message_text="cannot find people!!!"
			return m.to_json()
		m=MessageClass()
		for status in p:
			st=MessageAttachmentsClass()
			st.title=status.name
			scname=AttachmentFieldsClass()
			scname.value=status.screen_name
			st.attach_field(scname)
			u=AttachmentFieldsClass()
			u.value=status.profile_image_url
			st.attach_field(u)

			m.attach(st)
		return m.to_json()


	def status (self,args):
		tweet=args['tweet']
		try:
			self.api.update_status(tweet)
		except:
			m  = MessageClass()
			m.message_text="Status not updated!!!"
			return m.to_json()
		m=MessageClass()
		m.message_text="Status Updated!!!"
		return m.to_json()

	def unfavourite(self,args):
		id=args['id']
		try:
			self.api.destroy_favorite(id)
		except:
			m  = MessageClass()
			m.message_text="Status can't be added to unfavourites!!!"
			return m.to_json()
		m=MessageClass()
		m.message_text="Status with id="+ id+ " is added to unfavorites !!!"
		return m.to_json()

	def unfollow(self,args):
		handle=args['handle']
		try:
			self.api.destroy_friendship(handle)
		except:
			m  = MessageClass()
			m.message_text="can't unfollow!!!"
			return m.to_json()
		m=MessageClass()
		m.message_text="Person with screen_name="+handle+ " is unfollowed!!!"
		return m.to_json()

	