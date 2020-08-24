from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

def read_blog_list(request):  #이거 요청이 오면 blogs 에다가 다 담아넣어둠.
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 2)
    page = request.GET.get('page') #입력받은 page 를 page라는 새 변수에 넣는거구만.
    posts = paginator.get_page(page) #해당 페이지의 글들만 단체로 묶어서 보내주는거지.
    return render(request, 'post/blog_list.html', {'posts':posts}) #여기 변수 바꿨으니까 저 html만 수정해주면대네

def read_blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'post/blog_detail.html', {'blog':blog})

def blog_new(request):
    return render(request, 'post/blog_new.html')

def create_blog(request): #submit 했을때 하는 동작이지. ㅇㅇ, BLOG_ID (PK) 는 알아서 자동으로 채워질듯?? 맞냐??
    blog = Blog() #이 blog 라는 새로운 객체에다가 밑에 3개를 채우는거임.
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now() #근데 컴퓨터는 지금 시간을 어케 알까?
    blog.hash_tag = request.POST['hash_tag']
    blog.save()  # 이게 query method 중 하나래!! models.py 랑 db 연결,, 아!! 그니까 딱 이 한줄 때문에 객체 하나가 추가되는거네!!
    return redirect('read_blog_list')    #admin에도 뜨고 ㅇㅇ 다 하고나면 다시 list 로 돌아가게 해주는거넹.. (이건 함수곘네)


# 아 뒤에 저렇게 딕셔너리로 blog:blog 이렇게 써야지 저 html 로 가서 blogs 나 blog 변수 쓰면 여기서 가져가준다 그말이구나.
# blog_new 는 새로 만드는거라필요가 없지 매개변수, 페이지만 띄워주면 되니까

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete() #마찬가지로 이게 save()처럼 데이터베이스에서 지우는거겥네
    return redirect('read_blog_list')

def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    if request.method == "POST":
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.hash_tag = request.POST['hash_tag']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('read_blog_detail', blog_id)
    else:
        return render(request, 'post/blog_edit.html', {'blog':blog})