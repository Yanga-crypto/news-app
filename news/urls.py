from django.urls import path
from .views import (home,
                    journalist_dashboard, publisher_create,
                    publisher_delete,
                    publisher_detail,
                    newsletter_create,
                    newsletter_delete,
                    newsletter_update,
                    newsletter_detail,
                    newsletter_list,
                    article_list,
                    article_create,
                    article_delete,
                    article_update,
                    article_detail,
                    editor_dashboard,
                    editor_view_list,
                    approve_article,
                    approve_newsletter,
                    editor_delete,
                    editor_update,
                    reader_dashboard,
                    editor_view_list_newsletter,
                    editor_update_newletters,
                    editor_delete_newsletter,
                    reader_articles_view,
                    sub_journalist,
                    sub_publishers,
                    sub_to_journalist,
                    sub_to_publisher,
                    api_article_list,
                    )

urlpatterns = [
    path("", home, name="home"),
    path("journalist-dashboard/", journalist_dashboard, name="journalist_dashboard"),

    path("publisher/", publisher_create, name="publisher_create"),
    path('publisher-delete/', publisher_delete, name='publisher_delete'),
    path('publisher-detail/', publisher_detail, name='publisher_detail'),

    # URLS PATTERNS FOR NEWSLETTERS
    path('newsletter-create/', newsletter_create, name='newsletter_create'),
    path('newsletter-delete/<int:pk>/', newsletter_delete, name='newsletter_delete'),
    path('newsletter-update/<int:pk>/', newsletter_update, name="newsletter_update"),
    path('newsletter-list/', newsletter_list, name="newsletter_list"),
    path('newsletter-detail/<int:pk>/', newsletter_detail, name="newsletter_detail"),

    # URLS patterns for articels
    path("article-list/", article_list, name="article_list"),
    path('article-detail/<int:pk>/', article_detail, name='article_detail'),
    path('article-create/', article_create, name="article_create"),
    path('article-delete/<int:pk>/', article_delete, name='article_delete'),
    path('article-update/<int:pk>/', article_update, name='article_update'),

    # URLS patterns for editor articles
    path('editor-view-list/', editor_view_list, name='editor_view_list'),
    path("editor-update/", editor_update, name='editor_update'),
    path("editor-delete/", editor_delete, name='editor_delete'),
    path("editor-dashboard/", editor_dashboard, name="editor_dashboard"),
    path("approve-article/<int:pk>/", approve_article, name="approve_article"),
    path("approve-newsletter/<int:pk>/", approve_newsletter, name="approve_newsletter"),


    # URLS patterns for editor newsletters
    path('editor-view-list-newsletter/', editor_view_list_newsletter, name="editor_view_list_newsletter"),
    path('editor-update-newletters/', editor_update_newletters, name='editor_update_newletters'),
    path('editor-delete-newsletter/', editor_delete_newsletter, name="editor_delete_newsletter"),

    # URLS patterns for reader newsletters
    path("reader-dashboard/", reader_dashboard, name='reader_dashboard'),

    # URLS patterns for subscription to publishers and journalists
    path("sub-publishers/", sub_publishers, name="sub_publishers"),
    path("sub-journalists/", sub_journalist, name="sub_journalists"),
    path("sub-to-journalist/<int:pk>/", sub_to_journalist, name="sub_to_journalist"),
    path("sub-to-publisher/<int:pk>/", sub_to_publisher, name="sub_to_publisher"),

    # URL pattern for serializers
    path('api-articles/', api_article_list, name="api_articles"),
]
