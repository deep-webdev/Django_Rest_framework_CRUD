from django.contrib import admin
from django.urls import path, include
from . views import article_detail, article_list, article_list_view, article_detail_view, ArticleAPIView, ArticleDetails, GenericAPIView

urlpatterns = [
    # For Function Based View
    path('article/', article_list),
    path('details/<int:pk>', article_detail),
    path('browse_article/', article_list_view),
    path('browse_article_detail/<int:pk>', article_detail_view),
    
    # For Class Based View
    path('', ArticleAPIView.as_view()),
    path('detail_class/<int:id>', ArticleDetails.as_view()),
    
    # For Generic View
    path('generic/article/', GenericAPIView.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view())
    
]
