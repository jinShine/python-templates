from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>', views.board_detail),
    path('list/', views.baord_list),
    path('write/', views.baord_write),
]