from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from sportsnews.models import Article
from .forms import CommentForm

def article_list(request):
    articles = Article.objects.all().order_by('-published_at')
    return render(request, 'sportsnews/article_list.html', {
        'articles': articles,
    })

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.filter(active=True)

    new_comment = None
    if request.method == 'POST' and 'comment_submit' in request.POST:
        if not request.user.is_authenticated:
            return redirect('login')
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            return redirect('sportsnews:detail', pk=article.pk)
    else:
        comment_form = CommentForm()

    liked_by_user = False
    if request.user.is_authenticated:
        liked_by_user = article.likes.filter(id=request.user.id).exists()

    return render(request, 'sportsnews/article_detail.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
        'liked_by_user': liked_by_user,
    })

@login_required
def like_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    user = request.user
    if article.likes.filter(id=user.id).exists():
        article.likes.remove(user)
    else:
        article.likes.add(user)
    return redirect('sportsnews:detail', pk=pk)

