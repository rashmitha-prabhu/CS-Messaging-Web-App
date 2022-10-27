from django.urls import path

from users.views import *

urlpatterns = [
    path('', get_user_query),
    path('success/', success_page, name='success'),
]
