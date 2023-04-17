from django.urls import path
from flaskblog.__init__ import OrderView

urlpatterns = [
    
    path('reset_passwd/', OrderView.as_view(), name='order'),
]

