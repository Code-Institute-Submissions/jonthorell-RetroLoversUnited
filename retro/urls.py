
from urllib import request
from django.urls import path
from .views import Index, Links,Contact, About, Kategory, Create_article, Thankyou, Test, Edit_profile, View_profile,List_Users,Author

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('links', Links.as_view(), name='links'),
    path('contact',Contact.as_view(), name='contact'),
    path('about', About.as_view(), name='about'),
    path('category', Kategory.as_view(), name='Kategory'),
    path('create_article', Create_article.as_view(), name='Create_article'),
    path('test', Test.as_view(), name='test'),
    path('thankyou', Thankyou.as_view(), name='thankyou'),
    path('edit_profile', Edit_profile.as_view(), name='edit_profile'),
    path('view_profile', View_profile.as_view(), name='view_profile'),
    path('list_users', List_Users.as_view(), name='list_users'),
    path('author', Author.as_view(), name='author')
    ]