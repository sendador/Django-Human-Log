from django.contrib import admin
from django.urls import path, include
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index_page'),
    path('tinymce/', include('tinymce.urls')),
    path('post/', include('post.urls')),
]

