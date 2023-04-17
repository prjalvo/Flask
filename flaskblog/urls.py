from django.urls import path
from flaskblog.__init__ import User

urlpatterns = [
    
    path('reset_passwd/', User.as_view(), name='get_reset_token'),
]

