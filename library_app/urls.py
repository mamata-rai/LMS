
# from django.contrib import admin
# from django.urls import path
# from .views import *
# from library_app import views

# urlpatterns = [
#     # path('',views.home,name='home'),
#     path('', HomeView.as_view(), name='home'),
#     path('borrow/<int:book_id>/',views.borrow_book,name='borrow_book'),
#     path('return/<int:record_id>/',views.return_book,name='return_book'),
#     path('my_books/',views.my_books,name='my_books'),
#     # path('add-book/', views.add_book, name='add_book'),
#     path('add-book/', AddBookView.as_view(), name='add_book'),

#     path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'), 
#     path('signup/', views.signup_view, name='signup'),
#     path('login/', views.login_view, name='login'),


#     path('logout/', views.logout_view, name='logout'),
#     path("create-admin/", views.create_admin),
#     path('', views.home, name='home')
# ]



from django.urls import path
from .views import (HomeView, AddBookView, BorrowBookView, ReturnBookView,MyBooksView,ContactView, DeleteBookView, MembershipView,AboutView,SignupView,PostByCategory,CategoryBooksView)

urlpatterns = [

    path('', HomeView.as_view(), name='home'),

    path('borrow/<int:book_id>/', BorrowBookView.as_view(), name='borrow_book'),
    path('my_books/<int:book_id>/', MyBooksView.as_view(), name='my_books'),

    path('return/<int:issue_id>/', ReturnBookView.as_view(), name='return_book'),

    path('my_books/', MyBooksView.as_view(), name='my_books'),
    path('add-book/', AddBookView.as_view(), name='add_book'),

    path('delete-book/sdfvg/<int:pk>/', DeleteBookView.as_view(), name='delete_book'),
    path("membership/", MembershipView.as_view(), name="membership"),
    
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),


    
    path('post-by-category/<int:category_id>',PostByCategory.as_view(),name='post_by_category'),
        # path("post-by-category/<int:book_id>/",PostByCategory.as_view(),name="post_by_category"),
    path('categories/', CategoryBooksView.as_view(), name='category_list'),
    path("category/<int:id>/", CategoryBooksView.as_view(), name="category_books"),
        path('signup/', SignupView.as_view(), name='signup'),
]




