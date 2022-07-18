"""blog_project URL Configuration

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
from django.urls import path,include 
from rest_framework.schemas import get_schema_view # new for project schema
from rest_framework.documentation import include_docs_urls ## new for api docs 
from rest_framework_swagger.views import get_swagger_view ## new for swagger 
API_TITLE = 'Blog API'
API_DESCRIPTION = 'A web api for creating and editing blog posts made by Davis'
swagger_view = get_swagger_view(title=API_TITLE)  # new for schema api 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('posts.urls')),
    path('api-auth/',include('rest_framework.urls')), 
    path('api/rest_auth/',include('rest_auth.urls')),
    path('api/rest_auth/registration/',include('rest_auth.registration.urls')),
    path('docs/',include_docs_urls(title=API_TITLE,description=API_DESCRIPTION)), #new
    # path('schema/',schema_view),
    path('swagger-docs/',swagger_view)

     #new url for authentication
     #new auth login url 
]
