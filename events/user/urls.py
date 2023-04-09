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
    # path('event/', views.index),
    # path('event/info/', views.index),
    # path('event/insert/', views.index),
    # path('event/update/', views.index),
    # path('event/delete/', views.index),

    # Payment
    # path('payment/', views.index),
    # path('payment/info/', views.index),
    # path('payment/insert/', views.index),
    # path('payment/update/', views.index),
    # path('payment/delete/', views.index),
]
