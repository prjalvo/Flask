from django.urls import path
from flaskblog.models import OrderView

urlpatterns = [
    
    path('order/', OrderView.as_view(), name='order'),
]

