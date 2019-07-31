from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm

# Create your views here.
def home(request):
    posts = Post.objects
    return render(request, 'home/home.html', {'posts':posts})

def usa(request):
    posts = Post.objects
    return render(request, 'home/usa.html', {'posts':posts})

def uk(request):
    posts = Post.objects
    return render(request, 'home/uk.html', {'posts':posts})

def korea(request):
    posts = Post.objects
    return render(request, 'home/korea.html', {'posts':posts})

def detail(request,post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    form=CommentForm()
    return render(request, 'home/detail.html',{'post' : post_detail,'form':form,})

def ukdetail(request,post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    form=CommentForm()
    return render(request, 'home/ukdetail.html',{'post' : post_ukdetail,'form':form,})

def koreadetail(request,post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    form=CommentForm()
    return render(request, 'home/koreadetail.html',{'post' : post_koreadetail,'form':form,})

def post_new(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('detail',post_id=post.pk)
    else:
        form=PostForm()
    return render(request,'home/post_new.html',{'form':form})
    
def post_uknew(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('ukdetail',post_id=post.pk)
    else:
        form=PostForm()
    return render(request,'home/post_uknew.html',{'form':form})

def post_koreanew(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('koreadetail',post_id=post.pk)
    else:
        form=PostForm()
    return render(request,'home/post_koreanew.html',{'form':form})

def post_edit(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
    if request.method=="POST":
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.published_date=timezone.datetime.now()
            post.save()
            return redirect('detail',post_id=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request,'home/post_edit.html',{'form':form})

def post_ukedit(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
    if request.method=="POST":
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.published_date=timezone.datetime.now()
            post.save()
            return redirect('ukdetail',post_id=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request,'home/post_ukedit.html',{'form':form})

def post_koreaedit(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
    if request.method=="POST":
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.published_date=timezone.datetime.now()
            post.save()
            return redirect('koreadetail',post_id=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request,'home/post_koreaedit.html',{'form':form})

def post_delete(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    post.delete()
    return redirect('home')

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
    return redirect('detail', post_id=post.pk)

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = comment.post
    comment.delete()
    return redirect('detail', post_id=post.id)