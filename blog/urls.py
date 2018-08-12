from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.viewIndex,            name = 'index'),
    path('post/<str:title>/',       views.viewPost,             name = 'post'),
    path('category/<str:search>/',  views.viewSearchCategory,   name = 'categorySearch'),
    path('author/<str:search>/',    views.viewSearchAuthor,     name = 'authorSearch'),
    path('search/',                 views.viewSearch,           name = 'search'),

    # ------------------------------------------- #
    # Used to update certain elements on the page
    # ------------------------------------------- #

    path('search-title/',           views.search_titles,        name = 'searchTitle'),
    path('like-post/',              views.like_post,            name = 'likePost'),
]