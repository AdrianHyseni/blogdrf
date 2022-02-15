from django.urls import path
from django.urls.resolvers import URLPattern
from .views import BlacklistTokenView, CustomUserCreate


app_name = 'users'

urlpatterns = [
       path('register/', CustomUserCreate.as_view(), name="create_user"),
       path('logout/blacklist/', BlacklistTokenView.as_view(), name="blacklist"),
]



