from django.urls import path
from flaskblog.models import User

urlpatterns = [
    
    path(r'reset_passwd', User.as_view(), name='get_reset_token'),
]

