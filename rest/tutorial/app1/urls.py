from django.urls import path
from . import views

urlpatterns=[
    path('',views.api,),
    path('post/',views.Post),
    path('postindex/<int:index>',views.Postindex),
    path('update_post/<int:post_id>',views.update_post),
    path('delete_post/<int:index>',views.delete_post),
    path('class/',views.Apipost.as_view()),
    path('classput/<int:index>',views.PostViewDeleteView.as_view()),
    path('mixins/',views.postmixins.as_view()),
    path('mixins/<int:pk>/',views.reterview.as_view())
    
]