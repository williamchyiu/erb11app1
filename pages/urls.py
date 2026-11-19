from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path("", views.index, name="index"),  # <-- 結尾必須加上逗號
    path("about/", views.about, name="about"),
]