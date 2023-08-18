from django.urls import path
from .views import HomePageView, ProjectDetailView, AllProjetsView, ContactView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('all-projects/', AllProjetsView.as_view(), name="all-projects"),
    path('<int:pk>/project/',ProjectDetailView.as_view(), name="project-detail"),
    path('contact/', ContactView.as_view(), name= "contact"),
]
