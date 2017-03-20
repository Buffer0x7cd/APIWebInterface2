from django.conf.urls import url
from .views import index,signup
urlpatterns = [
    url(r'^', signup)
]
