from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from django.contrib import admin
admin.autodiscover()

from register import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'search.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^search/',include('register.urls')),
    url(r'^register/$',views.SingleRegister,name='single_register'),
    url(r'^thanks/$',views.thanks,name='thanks'),
    url(r'^login/$','django.contrib.auth.views.login',{'template_name':'search_login.html'},name='login'),
    url(r'^edit_profile/$',auth(views.EditProfile),name='edit_profile',),
    url(r'^group_register/$',views.GroupRegister,name='group_register'),
    url(r'^(?:home/|)$', views.home,name='home',),
    url(r'^logout',views.user_logout,name='logout'),
    url(r'^help/$',views.help,name='helptext'),

)
