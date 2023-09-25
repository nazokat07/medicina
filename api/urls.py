from django.urls import path
from .views import *
from rest_framework import routers
from .views import *


'''router = routers.DefaultRouter()

router.register('cafe', CafeViewSet, basename='cafe')
router.register('menu', MenuViewSet, basename='menu')
'''
'''urlpatterns = [
    path('cafe/list/', CafeList.as_view()),
    path('cafe/<int:pk>/', CafeDetail.as_view()),
    path('cafe/create/', CafePost.as_view()),
    path('cafe/update/<int:pk>/', CafePut.as_view()),
    path('cafe/delete/', CafeDelete.as_view()),
]'''

'''urlpatterns = [

] + router.urls'''

urlpatterns = [
    path('client/', ClientAPI.as_view(), name='client'),
    path('blog/', BlogAPI.as_view(), name='blog'),
    path('sponsor/', SponsorAPI.as_view(), name='sponsor')
]