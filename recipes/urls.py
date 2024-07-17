from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewHome.as_view(), name="home"), # recipes:home
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name="recipe"), # recipes:recipe
    path('recipes/category/<int:category_id>/', views.RecipeListViewCategory.as_view(), name="category"), # recipes:category
    path('recipes/search/', views.RecipeListViewSearch.as_view(), name="search"), # recipes:search
]