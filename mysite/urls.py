from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from blog.views import PostDetailView
from django.conf import settings

urlpatterns = [
    path('blog/<slug:slug>/',
         PostDetailView.as_view(),
         name='post_detail'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)