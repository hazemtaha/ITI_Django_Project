from django.conf.urls import url
from . import views
app_name = 'subscribtions'
urlpatterns = [
	url(r'^$', views.subscribtions, name='subscribtions'),
	url(r'^add_subscribtion/', views.add_subscribtion, name='add_subscribtion'),
	]
