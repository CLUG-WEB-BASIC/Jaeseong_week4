from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.read_blog_list, name='read_blog_list'),
    path('detail/<int:blog_id>', views.read_blog_detail, name='read_blog_detail'),
    path('new/', views.blog_new, name='blog_new'),
    path('create/', views.create_blog, name='create_blog'),
    path('delete/<int:blog_id>', views.delete_blog, name='delete_blog'),
    path('edit/<int:blog_id>', views.update_blog, name='update_blog'),
]

# url 패턴이긴 한데, 서버에 요청하는 url 도 있구나,, 그러네! 글 쓰고 저장하기 누르면 url 바껴서 요청을 보내고 다시 변경사항 적용된
# 후의 화면을 다시 보여주는 새로운 url로 가는구나.def __str__