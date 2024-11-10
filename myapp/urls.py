from django.urls import path
from . import views

#create a new url

urlpatterns=[
   path('home/',views.home, name='home'),
   path('about/',views.about),
   path('contact/',views.contact),
   path('out/',views.out),
   path('details/',views.details),
   path('index/',views.index),
   path('experiment/', views.experiment),
   path('experiment/<person>', views.experiment),
   path('experiment/<person>/greetings/<greet>',views.experiment_greet)
   
]
