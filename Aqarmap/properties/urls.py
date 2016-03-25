from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	#ex addProperty/5 - send <prop_id> as an arguments | [0-9]+ sequences of digits
	#url(r'^(?P<prop_id>[0-9]+)/$', views.details, name='prop_details'),
	url(r'^(?P<addProperty_id>[0-9])/$', views.addProperty, name='add'),
]