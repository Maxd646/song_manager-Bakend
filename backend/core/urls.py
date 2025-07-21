from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView
from songs.views import RegisterView  # ✅ Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/register/', RegisterView.as_view(), name='auth_register'),
    path('api/', include('songs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
