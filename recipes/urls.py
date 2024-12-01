
from django.urls import path
from . import views

# naming Convection
# 'app/model_viewtype'
# 'recipes/recipe_detail.html'
# recipe_form.html is naming convention of template as it will be used by create and upadate view
# also recipe_confirm_delete is alos a naming convection

urlpatterns = [
    # path('', views.home ,name="recipes-home"),
    path('', views.RecipeListView.as_view() ,name="recipes-home"),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view() ,name="recipe-detail"),
    path('recipe/create/', views.RecipeCreateView.as_view() ,name="recipes-create"),
    path('recipe/<int:pk>/update/', views.RecipeUpdateView.as_view() ,name="recipe-update"),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view() ,name="recipe-delete"),
    path('about/', views.about ,name="recipes-about"),
]
