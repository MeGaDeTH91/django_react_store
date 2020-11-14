from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from main_app.views.categories import ListCategoriesView
from main_app.views.customer import authenticate_user, CustomerRegister, user_change_role, user_change_status
from main_app.views.products import ListProductsView
from main_app.views.profile import profile_details, ProfileEdit

urlpatterns = [
    # User urls
    path('users/login/', obtain_jwt_token, name='users-login'),
    path('users/verify/', authenticate_user, name='users-verify'),
    path('users/all/', CustomerRegister.as_view(), name='users-all'),
    path('users/register/', CustomerRegister.as_view(), name='users-register'),
    path('users/change-role/<int:pk>/', user_change_role, name='users-change-role'),
    path('users/change-status/<int:pk>/', user_change_status, name='users-change-status'),

    # Profile urls
    path('profile-details/<int:pk>/', profile_details, name='profile-details'),
    path('profile-edit/<int:pk>/', ProfileEdit.as_view(), name='profile-edit'),

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
