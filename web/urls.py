from django.urls import path
from . import views

app_name = "web"
urlpatterns = [
    path("redirect_good/", views.redirect_good, name="redirect_good"),
    path("redirect_bad/", views.redirect_bad, name="redirect_bad"),
    path("redirect_result/", views.redirect_result, name="redirect_result"),
]
