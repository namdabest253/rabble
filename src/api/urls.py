from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='api-user-list'),
    path('subRabbles/', views.subRabble_list, name='api-subRabble-list'),
    path('subRabbles/!<str:identifier>/posts/', views.post_list, name='api-post-list'),
    
    path('users/<int:pk>/', views.user_detail, name='api-user-detail'),
    path('subRabbles/!<str:identifier>/', views.subRabble_detail, name='api-subRabble-detail'),
    path('subRabbles/!<str:identifier>/posts/<int:pk>/', views.post_detail, name='api-post-detail'),
    path("subrabbles/!<str:identifier>/posts/<int:pk>/likes", views.toggle_like, name="post-like-toggle"),
]

学生= ['海伦', '汤姆']