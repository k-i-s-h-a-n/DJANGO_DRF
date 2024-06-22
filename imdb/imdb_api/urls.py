from django.urls import path
from imdb_api import views

urlpatterns = [
    path('', views.homePage,name="homePage"),
    path("list/",views.movie_list,name="movie-list"),
    path("list/<int:pk>",views.movie_detail,name="movie-detail"),
    
]
   