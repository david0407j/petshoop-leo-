from django.urls import path

from petshoop.base.views import home, plano, assinar_plano


app_name = "base"
urlpatterns = [
    path("", home, name="home"),
    path("plano", plano, name="plano"),
    path("assinar/<str:tipo>/", assinar_plano, name="assinar_plano"),
]
