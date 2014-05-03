from djangorestframework.views import View
import models

class PassageView(View):

	def get(self, request, id):
		return models.Passage.objects.get(pk = id)