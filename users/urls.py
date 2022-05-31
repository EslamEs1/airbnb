from django.urls import path
from .views import SignupUserForm, profile, edit_profile, user_reservations, user_listing


app_name = 'users'

urlpatterns = [
    path('profile/signup/', SignupUserForm.as_view(), name='signup'),
    path('accounts/profile/', profile, name='profile'),
    path('profile/edit', edit_profile, name='edit_profile'),
    path('profile/booking', user_reservations, name='user_reservations'),
    path('profile/listing', user_listing, name='user_listing'),

]

