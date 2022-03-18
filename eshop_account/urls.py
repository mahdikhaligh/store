from django.urls import path

from .views import login_user, register_user,\
    log_out_user, user_account_main,\
    user_edit_account, user_sidebar


urlpatterns = [
    path('user-sidebar', user_sidebar, name='user_sidebar'),

    path('login', login_user),
    path('logout', log_out_user),
    path('register', register_user),
    path('user-account', user_account_main),
    path('user-edit-account', user_edit_account),
]
