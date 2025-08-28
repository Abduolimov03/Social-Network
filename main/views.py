from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.views.generic import TemplateView
from .models import Post


@login_required
def create_post(request):
    if request.method == "POST":
        body = request.POST.get("body")
        media = request.FILES.get("media")
        if body:
            post = Post.objects.create(user=request.user, body=body, media=media)
            return redirect("index")
    return redirect("index")


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by("-created")
        return context