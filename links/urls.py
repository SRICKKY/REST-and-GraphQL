from django.urls import path, include

from .views import index, detail, add_link, delete_link


urlpatterns = [
	path('',index, name='index'),
	path('<int:id>/',detail, name='detail'),
	path('add/', add_link, name='add_link'),
	path('delete/<int:id>/', delete_link, name='delete_link'),
]