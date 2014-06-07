from .core import Captcha
from .exceptions import CaptchaVerifyFailed

def check_captcha(field_name = 'captcha'):

	def outer(func):
		
		def inner(request, *args, **kwargs):
			captcha = Captcha(request)
			if not captcha.check(request.DATA.get(field_name, None)):
				raise CaptchaVerifyFailed
				
			func(request, *args, **kwargs)
			
		return inner
		
	return outer

