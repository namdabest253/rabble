from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import subRabble, Post, Community, PostLike
from .forms import PostForm

def index(request):
    default = get_object_or_404(Community, community_identifier="default")
    subrabbles = subRabble.objects.filter(community_id=default)
    context = {"subrabbles": subrabbles}
    
    return render(request, "rabble/index.html", context)

def profile(request):
    context = {"username" : str(request.user), "email": str(request.user.email)}
    
    return render(request, "rabble/profile.html", context)

def subrabble_detail(request, identifier):
    subrabble = get_object_or_404(subRabble, identifier=identifier)
    posts = Post.objects.filter(subRabble_id = subrabble)
    context = {"subrabble": subrabble,
               "posts" : posts}
    
    return render(request, "rabble/subrabble_detail.html", context)

def post_detail(request, identifier, pk):
    subrabble = get_object_or_404(subRabble, identifier=identifier)
    post = get_object_or_404(Post, pk=pk, subRabble_id=subrabble)

    user_has_liked = False
    if request.user.is_authenticated:
        user_has_liked = PostLike.objects.filter(post=post, user=request.user).exists()

    return render(request, "rabble/post_detail.html", {
        "subrabble": subrabble,
        "post": post,
        "user_has_liked": user_has_liked
    })
    
    # subrabble = get_object_or_404(subRabble, identifier=identifier)
    # post = get_object_or_404(Post, pk=pk, subRabble_id=subrabble)
    
    # context = {
    #     "subrabble": subrabble,
    #     "post": post
    # }
    
    # return render(request, "rabble/post_detail.html", context)

def post_create(request, identifier):
    subrabble = get_object_or_404(subRabble, identifier=identifier)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.account_id = request.user
            post.subRabble_id = subrabble
            post.save()
            return redirect("post-detail", identifier=identifier, pk=post.pk)
    else:
        form = PostForm()

    context = {
        "subrabble": subrabble,
        "form": form,
    }
    return render(request, "rabble/post_form.html", context)

def post_edit(request, identifier, pk):
    subrabble = get_object_or_404(subRabble, identifier=identifier)
    post = get_object_or_404(Post, pk=pk, subRabble_id=subrabble)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post-detail", identifier=identifier, pk=post.pk)
    else:
        form = PostForm(instance=post)

    context = {
        "subrabble": subrabble,
        "form": form,
    }
    return render(request, "rabble/post_form.html", context)
