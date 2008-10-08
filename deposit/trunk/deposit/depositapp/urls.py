from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    url(r'^admin/$', admin.site.root, name="admin_url"),
    url(r'^login/$', 'deposit.depositapp.views.login', name="login_url"),    
    url(r'^logout/$', 'deposit.depositapp.views.logout', name="logout_url"),
    url(r'^user/(?P<username>\w+)/(?P<command>\w+)$',
            'deposit.depositapp.views.user', name="user_command_url"),
    url(r'^user/(?P<username>\w+)$', 'deposit.depositapp.views.user', name="user_url"),
    url(r'^transfer/create(?P<transfer_type>\w+)$',
            'deposit.depositapp.views.create_transfer', name="create_transfer_url"),
    url(r'^transfer/(?P<transfer_id>\d+)/received$',
            'deposit.depositapp.views.transfer_received', name="transfer_received_url"),
    url(r'^transfer/(?P<transfer_id>\d+)$',
            'deposit.depositapp.views.transfer', name="transfer_url"),
    url(r'^transfer/$', 'deposit.depositapp.views.list_transfer',
            name="transfers_url"),
    url(r'^project/(?P<project_id>\d+)$', 'deposit.depositapp.views.project',
            name="project_url"),
    (r'^.*$', 'deposit.depositapp.views.index'),
)
