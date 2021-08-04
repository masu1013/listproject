from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostDelete, PostUpdate


urlpatterns = [
    path('list/', PostList.as_view(), name='list'),
    path('detail/<int:pk>/', PostDetail.as_view(), name='detail'),
    path('create/', PostCreate.as_view(), name='create'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='delete'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='update'),
]
