from .import views
from django.urls import path

app_name = 'laborec'

urlpatterns = [
  path('toppage/', views.toppage, name='toppage'),
  path('logintop/', views.logintop, name='logintop'),

  path('jikangaiList/', views.jikangaiList.as_view(), name='jikangaiList'),
  path('jikangaiList/<int:pk>/', views.jikangaiDetail.as_view(), name='jikangaiDetail'),
  path('jikangaiCreate/', views.jikangaiCreate.as_view(), name='jikangaiCreate'),
  path('jikangaiUpdate/<int:pk>/', views.jikangaiUpdate.as_view(), name='jikangaiUpdate'),
  path('jikangaiDelete/<int:pk>/', views.jikangaiDelete.as_view(), name='jikangaiDelete'),

  path('saikin/', views.saikin, name='saikin'),
  path('yuketuList/', views.yuketuList, name='yuketuList'),
  path('seikagaku/', views.seikagaku, name='seikagaku'),
  path('ketueki/', views.ketueki, name='ketueki'),
  path('byouri/', views.byouri, name='byouri'),
  path('siyakukanri/', views.siyakukanri, name='siyakukanri')
]