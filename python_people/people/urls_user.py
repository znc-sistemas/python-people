from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView
from people.models import UserProfile



urlpatterns = patterns('',
    url(r'^(?P<slug>\w+)/$', DetailView.as_view(model=UserProfile, slug_field='user__username'), name="user-profile"),
)