"""
URL configuration for quizsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from quiz.views import QuestionViewsets,CategoryViewsets
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('Questions',QuestionViewsets)
router.register('Categorys',CategoryViewsets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token', obtain_auth_token, name="auth_token"),
    path('', include(router.urls)),
   # path('category/', CategoryViewsets.as_view(), name='personne-create'),
]
