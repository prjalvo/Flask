from django.urls import path
from flaskblog.models import OrderView

urlpatterns = [
    
    path('reset_passwd/', OrderView.as_view(), name='order'),
]

