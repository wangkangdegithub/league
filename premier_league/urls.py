from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^premier/$',views.premier),
    url(r'^premier/article/(?P<article_id>[0-9]+)$',views.article_page,name='article_page'),
    url(r'^edit/$',views.edit_page,name='edit_page'),
    url(r'^edit/action$',views.edit_action,name='edit_action'),
    url(r'^premier/prediction$',views.prediction,name='prediction'),
]