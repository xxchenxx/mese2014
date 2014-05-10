from rest_framework import viewsets, decorators, renderers, response, mixins
import models, serializers

class BasePassageViewSet(viewsets.GenericViewSet):

	model = models.Passage
	serializer_class = serializers.PassageSerializer
	
	def get_queryset(self):
		_type = self.request.GET.get('type', '').upper()
		queryset = models.Passage.objects.all()
		if _type:
			queryset = queryset.filter(type = _type)
		return queryset	

class PassageRetrieveViewSet(BasePassageViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):

	renderer_classes = (renderers.TemplateHTMLRenderer,)
	
	def list(self, *args, **kwargs):
		response = super(PassageRetrieveViewSet, self).list(*args, **kwargs)
		response.template_name = 'webboard/passages.html'
		return response
		
	# def retrieve(self, *args, **kwargs):
		# response = super(PassageRetrieveViewSet, self).retrieve(*args, **kwargs)
		# response.template_name = 'webboard/passages/detail.html'
		# return response
	
class PassageAPIViewSet(BasePassageViewSet, viewsets.ModelViewSet):
	pass
	
class CommentAPIViewSet(viewsets.ModelViewSet):

	model = models.Comment
	serializer_class = serializers.CommentSerializer
	
	def get_queryset(self):
		passage_pk = int(self.kwargs['passage_pk'])
		return models.Passage.objects.get(pk = passage_pk).comments.all()