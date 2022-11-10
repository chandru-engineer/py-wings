from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [



    path('', views.home, name='home' ), 
    path('get_qa/<str:pk>/', views.qa_page, name='get_qa'), 






] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)