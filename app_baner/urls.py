from django.urls import path

from .views import BanerDetailApiView, BanerListApiView

urlpatterns = [
    path('detail/baner/<int:pk>/',BanerDetailApiView.as_view()),
    path('list/baner/',BanerListApiView.as_view())
]
