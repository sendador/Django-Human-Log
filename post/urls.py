from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:id>/', views.post, name='post_detail'),
    path('old/', views.posts, name='post_old'),
    path('all/', views.allPosts, name='post_all'),
    path('<cat>/', views.categories, name='categories_list'),


]
