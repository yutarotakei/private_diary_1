from django.urls import path

from . import views


app_name='diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name='inquiry'),
    path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
    path('dairy-create/', views.DiaryCreateView.as_view(), name="diary_create"),
    path('diary-upgrade/<int:pk>/', views.DiaryUpdateView.as_view(), name="diary_upgrade"),
    path('diary-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name="diary_delete"),
]
