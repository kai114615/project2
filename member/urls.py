from django.urls import path
from member import views

app_name = 'member'
urlpatterns = [
    path('', views.index, name='index'),
    path('mobile/', views.mobile, name='mobile'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete')


]
