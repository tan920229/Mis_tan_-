# 引入path
from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    # 目前还没有urls
    path('article-list/', views.article_list, name='article_list'),
    # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    # 安全删除文章
    path(
        'article-safe-delete/<int:id>/',
        views.article_safe_delete,
        name='article_safe_delete'
    ),
    # 点赞 +1
    path(
        'increase-likes/<int:id>/',
        views.IncreaseLikesView.as_view(),
        name='increase_likes'
    ),
    path('article-update/<int:id>/', views.article_update, name='article_update'),
    path('article-charts/', views.article_charts, name='article_charts'),
    path('article-btccharts/', views.article_btccharts, name='article_btccharts'),
    path('article-bitmexfg/', views.article_bitmexfg, name='article_bitmexfg'),
    path('article-bitmexfd/', views.article_bitmexfd, name='article_bitmexfd'),

]