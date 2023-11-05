from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.conf import settings



urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
]

handler404 = 'main.views.custom_404'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)