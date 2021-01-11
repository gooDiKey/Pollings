from django.urls import path
from . import views

app_name = 'pollingsapp'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:polling_id>/', views.poll, name = 'poll'),
    path('<int:polling_id>/question/<int:question_id>', views.question, name = 'question'),
    path('<int:polling_id>/results/', views.result, name = 'results'),
    path('<int:polling_id>/vote/', views.vote, name = 'vote'),
    path('account/create/', views.signUpView, name='signup'),
    path('account/login/', views.loginView, name='login'),
    path('account/signout/', views.signoutView, name='signout'),
]
