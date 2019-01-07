"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import path, include

from .views import permission_denied, register


login_params = {
    'template_name': 'users/login.html',
    'redirect_authenticated_user': True,
}

password_reset_params = {
    'template_name': 'users/password_reset.html',
}

urlpatterns = [
    path('', lambda request: redirect('books:index'), name='root'),
    path('login/', LoginView.as_view(**login_params), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('books/', include('books.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
]

handler403 = permission_denied