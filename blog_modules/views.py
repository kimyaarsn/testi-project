from django.shortcuts import render ,get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Count
from .models import (Blog,BlogCategory,BlogTag,)
from .forms import BlogCommentForm

# Create your views here.


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_modules/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
        queryset = Blog.objects.filter(
            is_active=True,
            is_delete=False
        ).select_related(
            'author',
            'category'
        ).prefetch_related(
            'tags'
        )

        category_name = self.kwargs.get('category')

        if category_name:
            queryset = queryset.filter(
                category__url_title__iexact=category_name
            )

        return queryset

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_modules/blog_details.html'
    context_object_name = 'blog'

    def get_queryset(self):
        return Blog.objects.filter(is_active=True,is_delete=False).select_related('author','category').prefetch_related('tags','comments')

    def get_object(self, queryset=None):
        blog = Blog.objects.get(
            url_title=self.kwargs.get('url_title'),
            is_active=True,
            is_delete=False
        )

        blog.visit_count += 1
        blog.save(update_fields=['visit_count'])

        return blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = BlogCategory.objects.filter(
            is_active=True,
            is_delete=False
        )



        context['popular_blogs'] = Blog.objects.filter(
            is_active=True,
            is_delete=False
        ).order_by('-visit_count')[:5]

        context['popular_tags'] = BlogTag.objects.annotate(
            blog_count=Count('blogs')
        ).order_by('-blog_count')[:10]
        context['comment_form'] = BlogCommentForm()

        context['comments'] = self.object.comments.all()

        return context

def blog_categories_component(request):
    categories = BlogCategory.objects.filter(
        is_active=True,
        is_delete=False
    ).annotate(
        blogs_count=Count('blogs')
    )

    return render(
        request,
        'blog_module/includes/blog_categories.html',
        {'categories': categories}
    )

def popular_blogs_component(request):
    popular_blogs = Blog.objects.filter(is_active=True,is_delete=False).order_by('-visit_count')[:5]
    return render(request,'blog_modules/component/popular_blog.html',{'popular_blogs': popular_blogs})


def popular_tags_component(request):
    popular_tags = BlogTag.objects.annotate(blog_count=Count('blogs')).order_by('-blog_count')[:10]

    return render(request,'blog_modules/component/popular_tag_blog.html',{'popular_tags': popular_tags})

def add_blog_comment(request, blog_id):
    blog = get_object_or_404(
        Blog,
        id=blog_id,
        is_active=True,
        is_delete=False
    )

    if request.method == 'POST':
        comment_form = BlogCommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)

            new_comment.blog = blog

            if request.user.is_authenticated:
                new_comment.user = request.user

            new_comment.save()

    return redirect(blog.get_absolute_url())