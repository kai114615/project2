from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about/<int:year>', views.about),
    path('details/<uuid:product_id>', views.details),
    path('blog/<path:publish>', views.blog),
    path('course/<slug:course_name>', views.course),
    path('show/', views.show, name='show'),
    path('abc/', views.abc, name='contact')
]