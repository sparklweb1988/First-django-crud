from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:id>', views.update, name='update'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>',views.delete,name='delete')
]
