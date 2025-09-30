from django.contrib import admin
from django.urls import path, include
from practic_app.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/hello/<name>/<int:year>/', hello, name='hello'),
]
