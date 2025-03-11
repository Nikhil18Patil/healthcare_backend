"""
URL configuration for healthcare_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view=get_schema_view(
    openapi.Info(
        title="Healthcare Backend SYSTEMS API",
        default_version="v1",
        description="api documentation for you Healthcare Backend app",
        contact=openapi.Contact(email='nikhilpatil18012004@gmail.com'),
        license=openapi.License(name='All Rights Reserved')  
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    #for register and login
    path('api/auth/', include('user_app.urls')),
    
    #for patient api handling
    path('api/patient/', include('patient_app.urls')),
    
    
    #for mapping for doctor to
    path('api/mappings/', include('mappings_app.urls')),
    
    
    # for doctor  related apis
    path('api/doctors/', include('doctor_app.urls')),
    
    
    #swagger
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name="redoc-documetation"),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-documentation")
]
