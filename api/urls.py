from django.urls import path,include
from .views import *


urlpatterns = [
    path('api/signup/', CreateUserView.as_view(), name='api-signup'),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    path('', include('api.urls')),
]