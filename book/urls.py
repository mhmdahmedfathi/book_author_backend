from django.urls import path
from . import views

urlpatterns = [
    path('addbook', views.AddBook.as_view()),
    path('dashboard', views.GetAuthorBooks.as_view()),
    path('<int:id>', views.BookViews.as_view()),
    path('', views.GetBooks.as_view()),
]