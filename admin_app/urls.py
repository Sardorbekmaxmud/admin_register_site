from django.urls import path
from .views import home_page, login_page, logout_page, SignUpView

urlpatterns = [
    path('', home_page, name='home-page'),
    path('login/', login_page, name='login-page'),
    path('logout/', logout_page, name='logout-page'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
