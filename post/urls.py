from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:id>/', views.post, name='post_detail'),
    path('old/', views.posts, name='post_old'),
    path('<cat>/', views.categories, name='categories_list'),
    path('', views.allPosts, name='post_all'),

]
