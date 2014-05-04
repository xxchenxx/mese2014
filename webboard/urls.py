from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('webboard.views',
	#url(r'^$'),
	url(r'^(\d+)/', views.PassageView.as_view()),
)
