from django.urls import path
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('country/', views.country),
    path('categories/', views.categories),
    path('cities/', views.cities),
    path('about/', views.about),
    path('about/<int:year>', views.about)
]