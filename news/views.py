from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Newsletter, Publisher
from .forms import PublisherForm, ArticleForm, NewsletterForm
from django.contrib.auth.models import User
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings
from .tweeter import send_new_tweet


@login_required
def home(request):
    return render(request, 'home.html')


# create a test_dashboard
@login_required
def journalist_dashboard(request):
    articles = Article.objects.filter(journalist=request.user)
    newsletters = Newsletter.objects.filter(writer=request.user)
    print(articles)
    print(newsletters)
    context = {
        "articles": articles,
        "newsletters": newsletters
    }
    return render(request, "journalist_dashboard.html", context)


# Create editor dashboard
@login_required
def editor_dashboard(request):
    articles = Article.objects.filter(is_approved=False)
    newsletters = Newsletter.objects.filter(is_approved=False)

    context = {
        "articles": articles,
        "newsletters": newsletters,
    }

    # render the context
    return render(request, "editor_dashboard.html", context)


@login_required
def approve_article(request, pk):
    if request.user.profile.role.lower() == "editor":
        article = get_object_or_404(Article, pk=pk)

        article.is_approved = True
        article.save()

        journalist = article.journalist
        sub_users = journalist.subscribed_users.all()
        print(sub_users)

        emails = [
            profile.user.email
            for profile in sub_users
            if profile.user.email
        ]
        print(emails)

        if emails:
            send_mail(
                f"New articles approved: {article.title}",
                f"{article.title} created by {article.journalist.username}",
                settings.DEFAULT_FROM_EMAIL,
                emails,
            )

        new_tweet = f"New article {article.title} approved\n{article.content}\nwriten by {article.journalist.username}."
        send_new_tweet(new_tweet)

        return redirect("editor_dashboard")
    else:
        return redirect("home")


@login_required
def approve_newsletter(request, pk):
    if request.user.profile.role.lower() == "editor":
        newsletter = get_object_or_404(Newsletter, pk=pk)
        newsletter.is_approved = True
        newsletter.save()
        return redirect("editor_dashboard")
    else:
        return redirect("home")


# Journalist CRUD articles
@login_required
def article_list(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
        "page_title": "List of Articles",
    }
    return render(request, "article_list.html", context)


@login_required
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "article_detail.html", {"article": article})


@login_required
def article_create(request):
    if request.user.profile.role == "journalist":
        if request.method == "POST":
            form = ArticleForm(request.POST)
            if form.is_valid():
                article = form.save(commit=False)
                article.journalist = request.user
                article.save()
                return redirect("article_list")
        else:
            form = ArticleForm()
        return render(request, "article_form.html", {"form": form})
    else:
        return redirect("article_list")


@login_required
def article_update(request, pk):
    if request.user.profile.role == "journalist":
        article = get_object_or_404(Article, pk=pk)
        if request.method == "POST":
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save(commit=False)
                article.save()
                return redirect("article_list")
        else:
            form = ArticleForm(instance=article)
        return render(request, "article_form.html", {"form": form})
    else:
        return redirect("article_list")


@login_required
def article_delete(request, pk):
    if request.user.profile.role == "journalist":
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return redirect("article_list")
    else:
        return redirect("article_list")


# Journalist CRUD newsletters
@login_required
def newsletter_list(request):
    newsletters = Newsletter.objects.all()
    context = {
        "newsletters": newsletters,
        "page_title": "List of Newsletter",
    }
    return render(request, "newsletter_list.html", context)


@login_required
def newsletter_detail(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)
    return render(request, "newsletter_detail.html", {"newsletter": newsletter})


@login_required
def newsletter_create(request):
    if request.user.profile.role == "journalist":
        if request.method == "POST":
            form = NewsletterForm(request.POST)
            if form.is_valid():
                newsletter = form.save(commit=False)
                newsletter.writer = request.user
                newsletter.save()
                return redirect("newsletter_list")
        else:
            form = NewsletterForm()
        return render(request, "newsletter_form.html", {"form": form})
    else:
        return redirect("newsletter_list")


@login_required
def newsletter_update(request, pk):
    if request.user.profile.role == "journalist":
        newsletter = get_object_or_404(Newsletter, id=pk)
        if request.method == "POST":
            form = NewsletterForm(request.POST, instance=newsletter)
            if form.is_valid():
                newsletter = form.save(commit=False)
                newsletter.save()
                return redirect("newsletter_list")
        else:
            form = NewsletterForm(instance=newsletter)
        return render(request, "newsletter_form.html", {"form": form})
    else:
        return redirect("newsletter_list")


@login_required
def newsletter_delete(request, pk):
    if request.user.profile.role == "journalist":
        newsletter = get_object_or_404(Newsletter, pk=pk)
        newsletter.delete()
        return redirect("newsletter_list")
    else:
        return redirect("newsletter_list")


# create sa viewv publisher, url, template, update the url
@login_required
def publisher_create(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PublisherForm()
    return render(request, "publisher_form.html", {"form": form})


@login_required
def publisher_detail(request):
    publisher = get_object_or_404(Publisher)
    return render(request, "publisher_detail.html", {"publisher": publisher})


@login_required
def publisher_delete(request):
    if request.user.profile.role == "reader":
        publisher = get_object_or_404(Publisher)
        publisher.delete()
        return redirect("publisher_list")
    else:
        return redirect("publisher_list")


@login_required
def publisher_list(request):
    publishers = Publisher.objects.all()
# Creating a context dictionary to pass data
    context = {
        "publishers": publishers,
        "page_title": "List of Publishers",
    }
    return render(request, "publisher_list.html", context)


# Editor CRUD for articles
@login_required
def editor_view_list(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
        "page_title": "List of Articles",
    }
    return render(request, "article_list.html", context)


@login_required
def editor_update(request, pk):
    if request.user.profile.role == "editor":
        article = get_object_or_404(Article, id=pk)
        if request.method == "POST":
            form = NewsletterForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save(commit=False)
                article.save()
                return redirect("article_list")
        else:
            form = ArticleForm(instance=article)
        return render(request, "article_form.html", {"form": form})
    else:
        return redirect("article_list")


@login_required
def editor_delete(request, pk):
    if request.user.profile.role == "editor":
        article = get_object_or_404(Article, id=pk)
        article.delete()
        return redirect("article_list")
    else:
        return redirect("article_list")


# Editor CRUD for newletters
@login_required
def editor_view_list_newsletter(request):
    newsletters = Newsletter.objects.all()
    context = {
        "newsletters": newsletters,
        "page_title": "List of Newsletters",
    }
    return render(request, "newsletter_list.html", context)


@login_required
def editor_update_newletters(request):
    if request.user.profile.role == "editor":
        newsletter = get_object_or_404(Newsletter)
        if request.method == "POST":
            form = NewsletterForm(request.POST, instance=newsletter)
            if form.is_valid():
                newsletter = form.save(commit=False)
                newsletter.save()
                return redirect("newsletter_list")
        else:
            form = NewsletterForm(instance=newsletter)
        return render(request, "newsletter_form.html", {"form": form})
    else:
        return redirect("newsletter_list")


@login_required
def editor_delete_newsletter(request):
    if request.user.profile.role == "editor":
        newsletter = get_object_or_404(Newsletter)
        newsletter.delete()
        return redirect("newsletter_list")
    else:
        return redirect("newsletter_list")


# CRUD FOR READER (They can only view newletters and articles)
# Create a reader dashboard
@login_required
def reader_dashboard(request):
    articles = Article.objects.filter(is_approved=True)
    newsletters = Newsletter.objects.filter(is_approved=True)
    context = {
        "articles": articles,
        "newsletters": newsletters,
    }
    # render the context
    return render(request, "reader_dashboard.html", context)


@login_required
def reader_newsletters_view(request):
    if request.user.profile.role == "reader":
        newsletters = Newsletter.objects.all()
        context = {
            "newsletters": newsletters,
            "page_title": "List of Newsletters",
        }
        return render(request, "newsletter_list.html", context)
    else:
        return redirect("newsletter_list")


# CRUD FOR READER
@login_required
def reader_articles_view(request):
    if request.user.profile.role == "reader":
        articles = Article.objects.all()
        context = {
            "articles": articles,
            "page_title": "List of Articles",
        }
        return render(request, "article_list.html", context)
    else:
        return redirect("article_list")


# CRUD for subscription
@login_required
def sub_publishers(request):
    sub_publishers = request.user.profile.subscribed_publishers.all()
    print(sub_publishers)
    context = {
        "publishers": sub_publishers,
    }
    return render(request, "subscribed_publishers.html", context)


@login_required
def sub_journalist(request):
    sub_journalists = request.user.profile.subscribed_journalists.all()
    context = {
        "journalists": sub_journalists,
    }
    return render(request, "subscribed_journalist.html", context)


@login_required
def sub_to_journalist(request, pk):
    journalist = get_object_or_404(User, id=pk)
    request.user.profile.subscribed_journalists.add(journalist)

    return redirect("reader_dashboard")


@login_required
def sub_to_publisher(request, pk):
    publisher = get_object_or_404(Publisher, id=pk)
    request.user.profile.subscribed_publishers.add(publisher)

    subscribed_users = publisher.profile_set.all()
    print(subscribed_users)

    return redirect("reader_dashboard")


@api_view(['GET'])
def api_article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
