from django.urls import path
from .views import SendMessage

urlpatterns = [
    path('', SendMessage, name='send_message'),
]
