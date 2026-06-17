from django.urls import path
from . import views 


urlpatterns=[
    path('',views.home,name='home'),
    path('category/<int:id>/',views.category_posts,name='category_posts'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('search',views.search,name='search'),
    path('register/',views.register,name='register'),
    path('login_page/',views.login_page,name='login_page'),
    path('logout_page/',views.logout_page,name='logout_page')
]