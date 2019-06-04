from django.contrib import admin
from django.urls import path
import wordcount.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.base, name="base"),
    path('home/', wordcount.views.home, name="home"),
    path('about/', wordcount.views.about, name="about"),
    path('result/', wordcount.views.result, name="result"),
    path('savefiles/', wordcount.views.savefiles, name="savefiles"),
    path('new/', wordcount.views.new, name="new"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
