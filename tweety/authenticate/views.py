from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from yellowant import YellowAnt
from django.conf import settings
from authenticate.models import UserToken
from authenticate_twitter.models import apitable
from .commandcenter import CommandCenter
from django.views.decorators.csrf import csrf_exempt
import json

screen_name=""
def RedirectToAuthenticationPage(request):
	global screen_name
	screen_name=request.session['twitter_screen_name']
	return HttpResponseRedirect("https://www.yellowant.com/api/oauth2/authorize/?client_id=%s&response_type=code&reddirect_url=%s"%(settings.YELLOWANT_CLIENT_ID,settings.YELLOWANT_REDIRECT_URL))

def yellowantRedirectUrl(request):

	code=request.GET.get("code",False)
	if code is False:
		return HttpResponse("Invalid Response")
	else:
		y = YellowAnt(app_key=settings.YELLOWANT_CLIENT_ID, app_secret=settings.YELLOWANT_CLIENT_SECRET,
                  access_token=None,
                  redirect_uri=settings.YELLOWANT_REDIRECT_URL)
		access_token_dict = y.get_access_token(code)
		access_token = access_token_dict['access_token']

		yellowant_user=YellowAnt(access_token=access_token)
		user_integration=yellowant_user.create_user_integration()
		profile=yellowant_user.get_user_profile()

		print(request.user)
		
		global screen_name
		ut=UserToken.objects.create(screen_name=screen_name,yellowant_token=access_token,yellowant_id=profile['id'],yellowant_integration_id=user_integration['user_application'])

		return HttpResponse("User is authenticated!!!")

@csrf_exempt
def apiurl(request):
	
	data = json.loads(request.POST.get('data'))
	service_application=data["application"]
	verification_token = data['verification_token']
	yellowant_user=data['user']
	

	row=UserToken.objects.get(yellowant_id=yellowant_user)
	
	twitter_name=row.screen_name

	print(twitter_name)
	row=apitable.objects.get(screen_name=twitter_name)

	if verification_token == settings.YELLOWANT_VERIFICATION_TOKEN:
		cc=CommandCenter(data["user"],data["application"],data["function_name"],data['args'],row)
		return HttpResponse(cc.parse())
	else:
		return HttpResponse(status=403)