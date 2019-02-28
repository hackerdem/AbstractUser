from django.urls import path
from .views import CreateUserView, DetailUserView, CreateDoneTemplateView

urlpatterns = [
    path('create', CreateUserView.as_view(), name='create'),
    path('detail/<pk>', DetailUserView.as_view(), name='detail'),
    path('create-done',CreateDoneTemplateView.as_view(), name='create-done')
]
