from django.urls import path
from users.views import *
urlpatterns = [
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('dashboard/', dashboard_view, name="dashboard"),
    path('logout/', logout_view, name="logout"),
]