from django.urls import path
from .views import SignupUserForm, profile, edit_profile


app_name = 'users'

urlpatterns = [
    path('profile/signup/', SignupUserForm.as_view(), name='signup'),
    path('accounts/profile/', profile, name='profile'),
    path('profile/edit', edit_profile, name='edit_profile'),

]

