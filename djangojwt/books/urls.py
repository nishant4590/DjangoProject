from django.urls import path
# from .views import BookCreateListView, BookRetrieveUpdateDestroyView, 
from .views import book_list_create, book_detail,StudentAPI


urlpatterns=[
    path('student/', StudentAPI.as_view()),
    # path('student/<int:pk>/', StudentAPI.as_view()),
    path('books/', book_list_create, name='book-list-create'),
    path('books/<int:pk>/', book_detail, name='book-details'),
    # path('books/',BookCreateListView.as_view(), name='book-list-create'),
    # path('books/<int:pk>/',BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]
