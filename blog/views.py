from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import FormMixin, CreateView
from django.urls import reverse_lazy
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib import messages


class PostListView(ListView):
    model = Post
    template_name = 'djblog/blog/post_list.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        list_post = Post.objects.all()
        paginator = Paginator(list_post, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        return context


class PostDetailView(FormView, DetailView):
    model = Post
    template_name = 'djblog/blog/post_detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['comments'] = Comment.objects.filter(post_id=self.get_object().pk).order_by('comment_date')
        return context

    def form_valid(self, form):
        comment = CommentForm(form.data)
        if form.is_valid():
            comment_form = form.save(commit=False)
            comment_form.post = self.get_object()
            comment_form.comment_date = timezone.now()
            comment_form.save()
            return redirect('blog:index')


class PostView(CreateView):
    model = Post
    template_name = 'djblog/blog/post_edit.html'
    form_class = PostForm

    def form_valid(self, form):
        if form.is_valid():
            form.pub_date = timezone.now()
            form.save()
            return super(PostView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Post created successfully..")
        return reverse_lazy("blog:index")


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'djblog/blog/post_edit.html', {'form': form})
