from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET, require_http_methods

# Create your views here.
from daryo.utils import *
from yangiliklar.models import Post


@require_GET
def post_list_page(request):
    posts = Post.objects.all()
    content = {'posts': posts}
    return render(request=request, template_name="news.html", context=content)


@require_POST
def post_create(request):
    title = request.POST['title']
    overview = request.POST['overview']
    body = request.POST['body']
    post = Post(title=title, overview=overview, body=body)
    post.save()
    return redirect("yangiliklar:news")


@require_GET
def post_create_page(request):
    return render(request, "create_post.html")


@require_GET
def post_detail_page(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'detaill.html', {'post': post})
