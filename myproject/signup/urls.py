from django.urls import path
from .views import SignUpView, UsersView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/', UsersView.as_view(), name='users'),
]
