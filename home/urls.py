from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('post/usa',views.usa, name='usa'),
    path('post/korea',views.korea, name='korea'),
    path('post/uk',views.uk, name='uk'),
    path('post/<int:post_id>/', views.detail, name='detail'),
    path('post/<int:post_id>/', views.ukdetail, name='ukdetail'),
    path('post/<int:post_id>/', views.koreadetail, name='koreadetail'),
    path('post/new/', views.post_new,name='new'),
    path('post/koreanew/', views.post_koreanew,name='koreanew'),
    path('post/uknew/', views.post_uknew,name='uknew'),
    path('post/<int:post_id>/edit/',views.post_edit,name='edit'),
    path('post/<int:post_id>/koreaedit/',views.post_koreaedit,name='koreaedit'),
    path('post/<int:post_id>/ukedit/',views.post_ukedit,name='ukedit'),
    path('post/<int:post_id>/delete',views.post_delete, name='delete'),
    path('post/<int:post_id>/comment/',views.add_comment,name='add_comment'),
    path('comment/<int:comment_id>/delete/',views.comment_delete,name='comment_delete'),
]
