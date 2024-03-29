from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from usersapp import views as user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_view.register, name='register'),
    path('profile/',user_view.profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name="usersapp/login.html"), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="usersapp/logout.html"), name='logout'),
    path('password-reset/',
                auth_views.PasswordResetView.as_view(template_name="usersapp/password_reset.html"),
                name='password_reset'),
    path('password-reset/done/',
                auth_views.PasswordResetDoneView.as_view(template_name="usersapp/password_reset_done.html"),
                name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
                auth_views.PasswordResetConfirmView.as_view(template_name="usersapp/password_reset_confirm.html"),
                name='password_reset_confirm'),
    path('password-reset-complete/',
                auth_views.PasswordResetCompleteView.as_view(template_name="usersapp/password_reset_complete.html"),
                name='password_reset_complete'),
    path('', include('blogapp.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
