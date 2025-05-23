from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path('blog/',include('app.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls'))
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

handler404 = 'main.views.custom_404_view'