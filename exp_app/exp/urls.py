from django.conf.urls import url
from . import views

# simplified the get_item_page_info url to just items/<item_id>, added
# get_many_items functino to return multiple items for the spalsh screen (currently that's hard-coded
# because i just load the 3 items from fixtures)
urlpatterns = [
    url(r'^item/get_info/(?P<item_id>[0-9a-z]+)/$', views.get_item_page_info, name='item-page-info'),
    url(r'^item/get_info/(?P<item_id>[0-9a-z]+)/(?P<username>.+)/$', views.get_item_page_info, name='item-page-info'),
    url(r'^items/get_by/(?P<field>[A-Za-z_]+)/(?P<criteria>[A-Za-z0-9]+)/$', views.get_filtered_items, name='filtered-results'),
    url(r'^user/create/$', views.create_user, name='create-user'),
    url(r'^user/login/$', views.log_in, name='log-in'),
    url(r'^user/logout/(?P<auth_id>[0-9a-z]+)/$', views.log_out, name='log-out'),
    url(r'^auth/(?P<auth_id>[0-9a-z]+)/$', views.authenticate, name='auth_id'),
    url(r'^item/create/(?P<username>.+)/$', views.create_listing, name='create-listing'),
    url(r'^item/search$', views.search_listings, name='search-listing'),
]
