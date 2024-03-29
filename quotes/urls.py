from django.urls import path

from . import views


app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>/', views.main, name='root_paginate'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('add_author', views.add_author, name='add_author'),
    path('add_quote', views.add_quote, name='add_quote'),
    path('authors/', views.authors, name='authors'),
    path('authors/page/<int:page>/', views.authors, name='authors_paginated'),
    path('author/<int:author_id>/delete/', views.delete_author, name='delete_author'),
    path('author/<int:author_id>/edit/', views.edit_author, name='edit_author'),
]
