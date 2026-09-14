from django.contrib import admin
from django.urls import path, include
from portfolio.task_manager import views
from portfolio.web_card.views import render_webcard
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("users/", include("portfolio.task_manager.users.urls")),
    path("statuses/", include("portfolio.task_manager.statuses.urls")),
    path("labels/", include("portfolio.task_manager.labels.urls")),
    path("tasks/", include("portfolio.task_manager.tasks.urls")),
    path("admin/", admin.site.urls),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("webcard/", render_webcard, name="webcard"),
]
