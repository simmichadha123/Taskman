from django.urls import path
from testapp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.RegisterPage.as_view(), name='register'),    
    path('login/', views.CustomLoginView.as_view(), name='login'),    
    path('logout/', views.LogoutView.as_view(next_page='login'), name='logout'),    
    path('', views.TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', views.TaskDelete.as_view(), name='task-delete'), 
    
]