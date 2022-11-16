from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.home, name='home' ), 
    path('get_qa/<str:pk>/', views.qa_page, name='get_qa'), 
    path('runcode/<str:pk>/', views.runcode, name='runcode'),
    path('runcode_', views.runcode_, name = 'runcode_'), 

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)