from django.urls import path

from . import views

urlpatterns = [
    # Index
    path('', views.index),

    # User
    path('user/insert/', views.user_insert),
    path('user/info/<int:id>/', views.user_info),
    path('user/update/<int:id>/', views.user_update),
    path('user/delete/<int:id>/', views.user_delete),

    # Event
    path('event/insert/', views.event_insert),
    path('event/info/<int:id>/', views.event_info),
    path('event/update/<int:id>/', views.event_update),
    path('event/delete/<int:id>/', views.event_delete),

    # Payment
    # path('payment/insert/', views.index),
    # path('payment/info/<int:id>/', views.index),
    # path('payment/update/<int:id>/', views.index),
    # path('payment/delete/<int:id>/', views.index),
]
