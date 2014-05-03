from django.conf.urls import patterns, include, url
import resources, views
from djangorestframework.views import ListOrCreateModelView
urlpatterns = patterns('webboard.views',
	url(r'^$', ListOrCreateModelView.as_view(resource=resources.PassageResource)),
	url(r'^(\d+)/', views.PassageView.as_view(resource = resources.PassageResource)),
)
