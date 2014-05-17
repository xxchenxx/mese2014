from rest_framework.permissions import BasePermission, SAFE_METHODS
from accounts.models import HasReportModel, Person

class HasReport(BasePermission):

	def has_permission(self, request, view):
		return request.user and isinstance(request.user.profile.info, HasReportModel)
		
class IsAdminUser(BasePermission):

	def has_permission(self, request, view):
		if request.method in SAFE_METHODS:
			return request.user
		else:
			return request.user and request.user.is_staff
			
class IsPerson(BasePermission):
	
	def has_permission(self, request, view):
		return request.user and isinstance(request.user.profile.info, Person)
		
class OwnsObject(BasePermission):
	
	def has_object_permission(self, request, view, obj):
		return request.user and isinstance(request.user.profile.info, Person) and obj.owner == request.user.profile.info
		
class HasFile(BasePermission):
	
	def has_object_permission(self, request, view, obj):
		user = request.user
		return user and getattr(user.profile.info, user.profile.info.reports_field).bulk_in([obj.pk]).exists()