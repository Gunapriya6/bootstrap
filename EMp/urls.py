from django.urls import path
from EMp import views

urlpatterns=[
     path('',views.home,name='hm'),
     path('abt/',views.about,name='ab'),
     path('cnt/',views.contact,name='ct'),
     path('log/',views.login,name='lg')
]