from rest_framework.exceptions import APIException

class BondPublished(APIException):

	status_code = 400
	default_details = "The bond has been published."