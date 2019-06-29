from django.contrib import admin
from django.urls import path, include
import blog, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('blog/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
]
