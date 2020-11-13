from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from main_app.views.categories import ListCategoriesView
from main_app.views.customer import authenticate_user, CustomerList, users_all, user_details, user_edit
from main_app.views.products import ListProductsView

urlpatterns = [
    # User urls
    path('users/login/', obtain_jwt_token),
    path('users/verify/', authenticate_user),
    path('users/all/', users_all),
    path('users/register/', CustomerList.as_view()),

    # Profile urls
    path('profile-details/<int:pk>/', user_details),
    path('profile-edit/<int:pk>/', user_edit),

    # Product urls
    path('products/all/', ListProductsView.as_view(), name='products-all'),

    # Category urls
    path('categories/all/', ListCategoriesView.as_view(), name='categories-all'),


    # # Expense pages
    # path('create/', expenses.expense_create, name='create expense'),
    # path('edit/<int:pk>', expenses.expense_edit, name='edit expense'),
    # path('delete/<int:pk>', expenses.expense_delete, name='delete expense'),
    #
    # # Profile pages
    # path('profile/', profiles.profile_details, name='profile details'),
    # path('profile/create/', profiles.profile_create, name='create profile'),
    # path('profile/edit/', profiles.profile_edit, name='edit profile'),
    # path('profile/delete/', profiles.profile_delete, name='delete profile'),
]
