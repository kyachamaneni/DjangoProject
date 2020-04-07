from django.urls import path
from . import views
from .views import SignUpView,UserUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    #path('changepersonalinfo', views.changepersonalinfo, name='changepersonalinfo'),
    #path('changepersonalinfo/<int:pk>/', changepersonalinfo.as_view(), name='changepersonalinfo'),
    path('<int:pk>/edit/',
         UserUpdateView.as_view(), name='Info_edit'),
    path('success/',views.success,name='success'),
]
