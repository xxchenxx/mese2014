from rest_framework.exceptions import APIException
from rest_framework import status
from common.exceptions import AssetsNotEnough
	
class SharesNotEnough(APIException):

	status_code = status.HTTP_400_BAD_REQUEST
	default_detail = 'The shares you have is not enough.'
	
class ParamError(APIException):
	
	status_code = status.HTTP_400_BAD_REQUEST