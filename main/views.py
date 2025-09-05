from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import PostForm, CommentForm
from .models import Post, Bookmark, Comment
from django.core.paginator import Paginator



@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'index'))

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, "post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form
    })

# 🔹 Post yaratish
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("index")
    else:
        form = PostForm()
    return render(request, "post_create.html", {"form": form})


# 🔹 Home sahifa (oxirgi postlar ko‘rinadi)
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # faqat 5 ta eng so‘nggi post
        context["posts"] = Post.objects.all().order_by("-created")[:5]
        return context


# 🔹 Postni bookmark qilish / o‘chirish
@login_required
def toggle_bookmark(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, post=post)

    if not created:  # agar allaqachon mavjud bo‘lsa → o‘chirish
        bookmark.delete()

    return redirect("bookmarks_list")


# 🔹 Foydalanuvchining saqlangan postlari
@login_required
def bookmarks_list(request):
    bookmarks = (
        Bookmark.objects.filter(user=request.user)
        .select_related("post", "post__user")  # extra join optimizatsiya
        .order_by("-created_at")
    )
    return render(request, "bookmarks.html", {"bookmarks": bookmarks})


@login_required
def post_list(request):
    posts = Post.objects.all().select_related("user").order_by("-created")
    paginator = Paginator(posts, 10)  # har sahifada 10 ta post
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "post_list.html", {"page_obj": page_obj})
