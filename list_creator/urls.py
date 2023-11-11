"""list_creator_forms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from lists.views import *
from django.conf import settings
from django.conf.urls.static import static

stat = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Lists
    path('', index, name='home'),
    path('add_list/', add_list),
    # path('delete_list/<int:l>/', delete_list),
    path('delete_list/<int:pk>/', DeleteListNameView.as_view()),
    # path('edit_list/<int:l>/', edit_list),
    # path('update_list/<int:l>/', update_list),
    path('edit_list/<int:pk>/', UpdateListNameView.as_view()),

    # Items
    path('list_page/<int:l>/', list_page, name='list_page'),
    path('add_item/<int:l>/', add_item),
    path('list_page/<int:l>/delete_item/<int:i>/', delete_item),
    # path('list_page/<int:l>/delete_item/<int:pk>/', DeleteListItemView.as_view()),
    path('list_page/<int:l>/edit_item/<int:i>/', edit_item),
    path('list_page/<int:l>/update_item/<int:i>/', update_item),

    # Authentication
    path("accounts/", include("django.contrib.auth.urls")),
    path('signup/', SignUpView.as_view(template_name='registration/signup.html'), name='signup'),
    path('demo_login/', demo_login, name='demo_login')
] + stat
