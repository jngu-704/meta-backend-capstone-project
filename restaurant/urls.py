# define URL route for index() view
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('booking/', views.BookingViewSet.as_view()),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),

]
