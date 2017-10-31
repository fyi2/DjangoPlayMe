from django.conf.urls import url
from django.contrib import admin
#from playme.core import views as core_views
from core import views as core_views
from django.contrib.auth import views as auth_views
from django.conf import settings

# SET THE NAMESPACE!
app_name = 'core'


urlpatterns = [
    url(r'^$', core_views.index, name='index'),
    url(r'signup/$', core_views.signup, name='signup'),
    url(r'snakeyes/$', core_views.snakeyes, name='snakeyes'),
    url(r'snakedone/$', core_views.snakedone, name='snakedone'),
    url(r'war/$', core_views.war, name='war'),
    url(r'peace/$', core_views.peace, name='peace'),
    url(r'^account/$', core_views.account, name='account'),
    url(r'^transfer/$', core_views.transfer, name='transfer'),
    url(r'^profile/$', core_views.view_profile, name='profile'),
    url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='user_login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/play/'}, name='logout'),
    url(r'^edit_account/$', core_views.edit_account, name='edit_account'),
    url(r'^edit_profile/$', core_views.edit_profile, name='edit_profile'),
    url(r'^change_password/$', core_views.change_password, name='change_password'),
]
