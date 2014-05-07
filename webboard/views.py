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
		response.template_name = 'webboard/passages/list.html'
		return response
		
	def retrieve(self, *args, **kwargs):
		response = super(PassageRetrieveViewSet, self).retrieve(*args, **kwargs)
		response.template_name = 'webboard/passages/detail.html'
		return response
	
class PassageUpdateViewSet(BasePassageViewSet, mixins.UpdateModelMixin):
	
	@decorators.link()
	def comments(self, request, pk = None, *args, **kwargs):
		comments = models.Comment.objects.filter(passage__pk = pk)
		serializer = serializers.PaginatedCommentSerializer(comments, many = True)
		return response.Response(serializer.data)
	
class CommentViewSet(viewsets.ModelViewSet):

	model = models.Comment
	serializer = serializers.CommentSerializer