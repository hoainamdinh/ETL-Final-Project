from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload'),  # Đảm bảo không có 'ETL/' ở đầu
]

urlpatterns += [
    path('display/', views.display_data, name='display'),
]
