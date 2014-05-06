from rest_framework import viewsets
import models, serializers

class PassageViewSet(viewsets.ModelViewSet):

	model = models.Passage
	serializer_class = serializers.PassageSerializer
	
	def get_queryset(self):
		_type = self.request.GET.get('type', '').upper()
		print _type
		queryset = models.Passage.objects.all()
		if _type:
			queryset = queryset.filter(type = _type)
		print queryset
		return queryset