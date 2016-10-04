from django.conf.urls import url
import views
# Create your views here.

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/register/$', views.register, name='register'),
    url(r'^/login/$', views.user_login, name='login'),
]

