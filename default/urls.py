from django.urls import path
from . import views

urlpatterns = [
    # path('poll/', views.poll_list),
    path('poll/', views.PollList.as_view()),
    path('poll/<int:pk>/', views.PollView.as_view()),
    path('option/<int:oid>/', views.PollVote.as_view()),#投票選項編號，取整數然後輸入到OID裡
    path('poll/create/', views.PollCreate.as_view()),
    path('poll/<int:pk>/edit/', views.PollEdit.as_view()),

]