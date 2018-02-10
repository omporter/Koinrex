from django.conf.urls import url
from django.urls import re_path

from . import views

app_name = 'users'
urlpatterns = [
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    re_path(r'^(?P<username>[\w.@+-]+)/$',
            views.UserDetailView.as_view(),
            name='detail'
            ),
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
]
