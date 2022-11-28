from django.contrib import admin
from django.urls import path
from .views import index,success

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="home"),
    path("success/",success,name="success_page")
]
