from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/addpage', views.AddPage.as_view()),
    path('<slug:slug>/<int:id>/', views.GetBooksPages.as_view()),
    path('<slug:slug>/<int:id>/views', views.PageViews.as_view()),
]