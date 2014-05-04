from rest_framework import generics
import models, serializers

class PassageView(generics.ListAPIView):

	queryset = models.Passage.objects.all()
	serializer_class = serializers.PassageSerializer