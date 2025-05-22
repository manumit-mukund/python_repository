from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("my_hello_app/", include("my_hello_app.urls")),
    path("admin/", admin.site.urls),
]