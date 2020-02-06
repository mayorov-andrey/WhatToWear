"""whattodo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from about.views import AboutView
from contacts.views import ContactsView
from howtobuy.views import HowToBuyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('', include('main.urls')),
    path('guestbook/', include('guestbook.urls')),
    path('news/', include('news.urls')),
    path('imagepool/', include('imagepool.urls')),
    path('categories/', include('categories.urls')),
    path('goods/', include('goods.urls')),
    path('comments/', include('django_comments.urls')),
    path('blog/', include('blog.urls')),
    path('about/', AboutView.as_view(), name="about"),
    path('contacts/', ContactsView.as_view(), name="contacts"),
    path('howtobuy/', HowToBuyView.as_view(), name="howtobuy"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
