from django.contrib import admin
from django.urls import path, include
from mysite.app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secret/', views.secret_page, name='secret_page'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
]
