from django.urls import path
from .views import (
    home_view,
    VueloListView,
    VueloDetailView,
    VueloDeleteView,
    VueloUpdateView,
    VueloCreateView,
    user_login_view,
    user_logout_view,
    UserUpdateView,
    vuelo_search_view,
    avatar_view,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("vuelo/list/", VueloListView.as_view(), name="vuelo-list"),
    path("vuelo/create/", VueloCreateView.as_view(), name="vuelo-create"),
    path("vuelo/<int:pk>/detail/", VueloDetailView.as_view(), name="vuelo-detail"),
    path("vuelo/<int:pk>/delete/", VueloDeleteView.as_view(), name="vuelo-delete"),
    path("vuelo/<int:pk>/update/", VueloUpdateView.as_view(), name="vuelo-update"),
    path('vuelo/buscar', vuelo_search_view, name="vuelo-buscar"),
    path("login/", user_login_view, name="login"),
    path("logout/", user_logout_view, name="logout"),
    path('editar-perfil/', UserUpdateView.as_view(), name='editar-perfil'),
    path('avatar/add/', avatar_view, name='avatar_add'),
]