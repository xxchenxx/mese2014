def identify_user(request, user):
	if not request.user.is_authenticated():
		return False
	return request.user.id == user.id