from django.shortcuts import render, redirect
from . models import Post
from . forms import commentForm
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/front.html', {
        'posts': posts
    })
    
    

def post_detial(request, slug):
    post = Post.objects.get(slug=slug)
    
    if request.method == "POST":
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_d', slug=post.slug)
    else:
        form = commentForm()
    return render(request, 'blog/detail.html', {
        'post': post,
        'form': form
    })
    

