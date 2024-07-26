from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('about/<int:year>', views.about),
    path('details/<uuid:product_id>', views.details),
    path('blog/<path:publish>', views.blog),
    path('course/<slug:course_name>', views.course)
]