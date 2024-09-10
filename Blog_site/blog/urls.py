from django.urls import path # type: ignore
from .views import *
urlpatterns = [
    path('', blogs, name="blogs"),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('logout/', logout_view, name="logout"),
]
