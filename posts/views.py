from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

def get_posts(request):
    """
    A list of posts that will be rendered to blogpost.html
    """
    
    posts = Post.objects.filter(published_date__lte=timezone.now
        ()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})
    

def post_detail(request, pk):
    """
    detailed post that will be rendered to postdetail.html
    or return 404
    """
    
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})

def create_or_edit_post(request, pk=None):
    """
    create or edit a post and will be rendered to postdetail.html or
    return a 404
    """
    
    post = get_object_or_404(Post, pk=pk) if pk else None
    
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.instance.author = request.user
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})
