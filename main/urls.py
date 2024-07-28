from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contestinfo/', views.contestinfo, name='contestinfo'),
    path('contest/', views.contest, name='contest'),
    path('contest/level2/', views.level2, name='level2'),
    path('contest/level3/', views.level3, name='level3'),
    path('contest/level4/', views.level4, name='level4'),
    path('contest/level5/', views.level5, name='level5'),
    path('contest/level6/', views.level6, name='level6'),
    path('contest/level7/', views.level7, name='level7'),
]
