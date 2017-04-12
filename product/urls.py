from django.conf.urls import patterns,include,url
from .import views
from django.views.static import serve
from django.conf import settings
app_name='product'

urlpatterns =[
	url(r'^$', views.home, name='home'),
	url(r'^home/$', views.home, name='home'),
	url(r'^signup/$',views.signup,name='signup'),
	url(r'^delete/(?P<id>\d+)/$',views.delete,name='delete'),
	url(r'^update/(?P<id>\d+)/$',views.update,name='update'),
	url(r'^Updateproduct/$',views.Updateproduct,name='updateproduct'),
	url(r'^sign/$',views.sign,name='sign'),
	url(r'^Addproduct/$',views.addproduct,name='addproduct'),
	url(r'^home/Addproduct/$',views.addproduct,name='addproduct'),
	url(r'^productinformation/(?P<id>\d+)/$',views.productinformation,name='productinformation'),
	url(r'^detailproduct/$',views.detailproduct,name='products'),
	url(r'^home/productlisting/$',views.productlisting,name='productlisting'),
	url(r'^productlisting/$',views.productlisting,name='productlisting'),
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),

]
