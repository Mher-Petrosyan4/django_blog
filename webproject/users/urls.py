from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users import views

urlpatterns = [
    path('', views.user_login, name="user-login"),
    path("register/", views.register, name="user-register"),
    path('logout/', views.user_logout, name='user-logout'),
    path("users/profile/", views.user_profile, name="user-profile"),
    path("users/profile/update", views.update_profile, name="update-profile"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)