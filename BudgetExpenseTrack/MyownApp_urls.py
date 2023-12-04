from django.urls import path,include
from BudgetExpenseTrack import views
from .views import UsersApi ,CategoryApi
urlpatterns=[
    path('UsersApi',UsersApi.as_view()),
    path('UsersApi/<int:user_id>',UsersApi.as_view()),
    path('CategoryApi/<int:category_id>',CategoryApi.as_view()),
    path('CategoryApi',CategoryApi.as_view()),
    path('',views.home,name='home')
]