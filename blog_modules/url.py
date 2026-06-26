from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.BlogListView.as_view(),
        name='blog_list'
    ),

    path(
        'category/<str:category>/',
        views.BlogListView.as_view(),
        name='blog_category'
    ),

    path(
        '<str:url_title>/',
        views.BlogDetailView.as_view(),
        name='blog_detail'
    ),
path(
    'add-comment/<int:blog_id>/',
    views.add_blog_comment,
    name='add_blog_comment'
),
]