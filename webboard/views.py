from rest_framework import viewsets, decorators, renderers, response, mixins
from rest_framework.generics import get_object_or_404
import models, serializers
import json

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
		response.template_name = 'wb/passages.html'
		return response
	
class PassageAPIViewSet(BasePassageViewSet, viewsets.ModelViewSet):
	
	def create(self, request, *args, **kwargs):
		request.DATA['author'] = request.user.id
		return super(PassageAPIViewSet, self).create(request, *args, **kwargs)

	def list(self, request, *args, **kwargs):
		self.serializer_options = {'exclude':['content']}
		return super(PassageAPIViewSet,self).list(self,request,*args,**kwargs)
	
class CommentAPIViewSet(viewsets.ModelViewSet):

	model = models.Comment
	serializer_class = serializers.CommentSerializer
	
	def get_queryset(self):
		passage_pk = int(self.kwargs['passage_pk'])
		return get_object_or_404(models.Passage, pk = passage_pk).comments.all()
		
	def create(self, request, *args, **kwargs):
		request.DATA['passage'] = int(kwargs['passage_pk'])
		request.DATA['author'] = request.user.id
		return super(CommentAPIViewSet, self).create(request, *args, **kwargs)