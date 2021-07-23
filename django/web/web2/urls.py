

from django.urls import path
from web2 import views as local_views
from post import views as post_views


urlpatterns = [
    
    #path('hello/', local_views.hi),
    path('sorted/',local_views.sorted),
    path('say_hi/<str:name>/<int:age>/',local_views.say_hi),
    path('post/',post_views.list_post),

]
