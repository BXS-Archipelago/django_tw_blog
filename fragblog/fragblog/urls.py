
from django.contrib import admin
from django.urls import path

from core.views import frontpage, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', frontpage, name='frontpage'),
]
