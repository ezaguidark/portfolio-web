from django.urls import path
from .views import (
    HomePageView, 
    ProjectDetailView, 
    AllProjetsView, 
    ContactView, 
    SuccessView, 
    BlogPostView,
    EasterEgg,
    Download_cv,
) 

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('all-projects/', AllProjetsView.as_view(), name="all-projects"),
    path('project/<slug:urlname>/',ProjectDetailView.as_view(), name="project-detail"),
    path('blog-post/<slug:urlname>/',BlogPostView.as_view(), name="post"),
    path('contact/', ContactView.as_view(), name= "contact"),
    path('contact/success/', SuccessView.as_view(), name= "success"),
    path('cv/', Download_cv, name= "cv"),
    path('easter-egg/', EasterEgg.as_view(), name="no-debi"),
]
