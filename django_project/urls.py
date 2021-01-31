from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Rest Framework urls
    path('', include('blog.urls')),  # Blogs App endpoints
    path('api/', include('blog_api.urls')),   # Blog API endpoints
]
