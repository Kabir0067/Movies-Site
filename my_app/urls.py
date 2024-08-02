from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),  
    path('category/new/', CategoryCreateView.as_view(), name='category_create'),  
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),  
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'), 
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    
    path('', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/new/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/<int:pk>/edit/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
    path('search/', VideoSearchView.as_view(), name='video_search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
