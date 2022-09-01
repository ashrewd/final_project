from django.contrib import admin
from django.urls import path

from user.views import index, login_view, logout_view, register_view, user_list_view
from final_project.settings import DEBUG

# if DEBUG:
#     import debug_toolbar
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("users/", user_list_view, name="user_list"),
]

# if DEBUG:
#     urlpatterns += [
#         path("__debug__/", include(debug_toolbar.urls)),  # Django Debug Tool
#     ]
