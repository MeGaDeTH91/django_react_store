from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from main_app.views.customer import current_user, CustomerList
from main_app.views.products import ListProductsView

urlpatterns = [
    # Product urls
    path('products', ListProductsView.as_view(), name='products-all'),

    path('token-auth/', obtain_jwt_token),
    path('current_user/', current_user),
    path('users/', CustomerList.as_view())

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
