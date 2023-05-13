from django.urls import path
from .views import UserView, Users, CreateUser, PostsView

urlpatterns = [
    path('users/<int:id>', UserView.as_view()),
    path('users/', Users.as_view()),
    path('create-user/', CreateUser.as_view()),
    path('posts/', PostsView.as_view()),
]
