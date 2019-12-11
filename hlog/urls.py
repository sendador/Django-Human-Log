from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index_page'),
    path('tinymce/', include('tinymce.urls')),
    path('post/<int:id>/', views.post, name='post_detail'),
    path('posts/old/', views.posts, name='post_old'),
    path('posts/<cat>/', views.categories, name='categories_list'),
    path('posts/', views.allPosts, name='post_all'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
