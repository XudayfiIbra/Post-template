from django.urls import path
from .  import views
urlpatterns = [
    path('', views.home, name="homePage"),
    path('blog-detail/<slug>', views.post_detial, name="post_d")
]
