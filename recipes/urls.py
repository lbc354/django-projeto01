from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"), # recipes:home
    path('recipes/<int:id>/', views.recipe, name="recipe"), # recipes:recipe
    path('recipes/category/<int:category_id>/', views.category, name="category"), # recipes:category
    path('recipes/search/', views.search, name="search"), # recipes:search
]