from rest_framework.exceptions import APIException

class MoneyNotEnough(APIException):
	
	status_code = 400
	default_detail = 'The money in your account is not enough.'
	
class SharesNotEnough(APIException):
	
	status_code = 400
	default_detail = 'The shares you have is not enough to be sold.'