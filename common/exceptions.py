from rest_framework.exceptions import APIException
from rest_framework import status

class AssetsNotEnough(APIException):
	
	status_code = status.HTTP_400_BAD_REQUEST
	default_detail = 'The assets in your account is not enough.'
	
class ParamError(APIException):
	
	status_code = status.HTTP_400_BAD_REQUEST