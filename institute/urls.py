from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'institute'  # Namespace for this app

urlpatterns = [
    path("institute-list/", institute_list, name="institute_list"),
    path("create_institute/", create_institute, name="create_institute")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)