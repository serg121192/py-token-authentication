from django.urls import path

from user.views import CreateTokenView, CreateUserView, ManageUserView


app_name = "user"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="get-token"),
    path("me/", ManageUserView.as_view(), name="manage"),
]
