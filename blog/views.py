from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect


def Post_list(request):
    Posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/Post_list.html' , {'Posts': Posts})




def Post_detail(request,pk):
    Postc= get_object_or_404(Post, pk=pk)
    Post.objects.get(pk=pk)
    return render(request,'blog/Post_detail.html',{'Postc':Postc})


def Post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
                        if form.is_valid():
                            Post = form.save(commit=False)
                            Post.author = request.user
                            Post.save()
                            return redirect('Post_detail', pk=Post.pk)
                        else:
                            form = PostForm()
                            return render(request, 'blog/Post_edit.html',{'form':form})


def Post_edit(request, pk):
    Post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostFrom(request,POST,instance=Post)
        if form.is valid():
            Post = form.save(commit=False)
            Post.author = request.user
            Post.save()
            return redirect('Post_detail', pk=Post.pk)
        else:
            form = PostForm(instance=Post)
            return render(request,'blog/Post_edit.html',{'form'})


def Post_draft_list(request):
    Posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request,'blog/Post_draft_list.html',{'Posts':Posts})


def Post_publish(request, pk):
    Post = get_object_or_404(Post, pk=pk)
    Post.publiush()
    return redirect('Post_detail', pk=Post.pk)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def Post_remove(request, pk):
    Post = get_object_or_404(Post, pk=pk)
    Post.delete()
    return redirect('Post_list')
