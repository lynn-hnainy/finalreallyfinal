"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from members import views as member_views
from adminPanel import views as admin_view
from books import views as book_views
from booksTransaction import views as booksTrans_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('register/', member_views.register, name='register'),
    path('', member_views.signin, name='login'),
    path('logout_member',member_views.logout_member,name="logout_member"),
    path('home',book_views.home,name="home"),
    path('list_books/<cat_id>',book_views.list_books,name="list_books"),
    path('search',book_views.search_books,name="search_books"),
    path('borrow/<book_id>/<user_id>',booksTrans_view.borrow_book,name="borrow_book"),
    path('reserve/<book_id>/<user_id>',booksTrans_view.reserve_book,name="reserve_book"),
    path('borrowed_books/<user_id>',booksTrans_view.borrowed_books,name="borrowed_books"),
    path('reserved_books/<user_id>',booksTrans_view.reserved_books,name="reserved_books"),
    path('renew_borrowing/<book_id>/<user_id>',booksTrans_view.renew_borrowing,name="renew_borrowing"),
    path('cancel_reservation/<book_id>/<user_id>',booksTrans_view.cancel_reservation,name="cancel_reservation"),
    path('book_detail/<book_id>', book_views.book_detail, name='book_detail'),
    path('books/<author_name>', book_views.books_author, name='books_author'),
    path('adminPanel', admin_view.welcome, name='admin_welcome'),
    path('adminPanel/search_user', admin_view.search_user, name='search_user'),
    path('adminPanel/books_byUser/<user>', admin_view.user_books, name='user_books'),
    path('adminPanel/return_book/<book_id>/<user_id>', admin_view.return_book,name='return_book'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name='password_reset_complete'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
