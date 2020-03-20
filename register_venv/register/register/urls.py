from django.contrib import admin
from django.urls import path, include
from signup.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('register/', include('signup.urls'))
]
