from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('profile/<int:id>/',views.profile,name='profile'), 
    path('',views.review_form,name='review' ),
    path('search/', views.search_results, name='search_results') 
    
    
    

    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)