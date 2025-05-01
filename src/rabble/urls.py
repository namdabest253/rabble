from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("!<slug:identifier>/", views.subrabble_detail, name="subrabble-detail"),
  path("!<slug:identifier>/<int:pk>/", views.post_detail, name="post-detail"),
  path("!<slug:identifier>/new", views.post_create, name="post-create"),
  path("!<slug:identifier>/<int:pk>/edit", views.post_edit, name="post-edit"),
  path("profile", views.profile, name="profile"),
  path("admin/", admin.site.urls),
  # path("", include("rabble.urls")),
  path("api/", include("api.urls"))
]
