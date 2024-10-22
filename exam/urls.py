from django.urls import path

from exam.views import UserView

urlpatterns = [
    path('user/', UserView.as_view({'get': 'list'}), name='user'),
]