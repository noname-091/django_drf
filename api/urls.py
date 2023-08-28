from django.urls import path
from .views import BookApiView, AddBookApiView, DeleteApiView

urlpatterns = [
    path('', BookApiView.as_view()),
    path('/add', AddBookApiView.as_view()),
    path('/del', DeleteApiView.as_view()),

]