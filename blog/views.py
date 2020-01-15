from django.shortcuts import render
from .models import Category, Article, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown
# Create your views here.


#首页
def index(request):
    allcategory = Category.objects.filter(article__is_active=True)
    allarticle = Article.objects.filter(is_active=True).order_by('-id')
    alltag = Tag.objects.distinct().filter(article__is_active=True)

    list = page_list(request, allarticle)
    return render(request, 'index.html', locals())  # 把上下文传到index.html页面


# 归档页
def archives(request):
    allcategory = Category.objects.filter(article__is_active=True)
    allarticle = Article.objects.filter(is_active=True).order_by('-id')
    alltag = Tag.objects.distinct().filter(article__is_active=True)

    list = page_list(request, allarticle)
    return render(request, 'archives.html', locals())


# 分类页
def categories(request):
    allcategory = Category.objects.filter(article__is_active=True)
    allarticle = Article.objects.filter(is_active=True).order_by('-id')
    alltag = Tag.objects.distinct().filter(article__is_active=True)

    categories = allcategory
    return render(request, "categories.html", locals())


# 分类详情页
def category_info(request,categoryId):
    allcategory = Category.objects.filter(article__is_active=True)
    allarticle = Article.objects.filter(is_active=True).order_by('-id')
    alltag = Tag.objects.distinct().filter(article__is_active=True)

    list = Article.objects.filter(category_id=categoryId, is_active=True) #获取通过URL传进来的lid，然后筛选出对应文章
    category = Category.objects.get(id=categoryId)#获取当前文章的栏目名
    list = page_list(request, list)
    return render(request, 'category_info.html', locals())


# 标签页
def tags(request):
    allcategory = Category.objects.filter(article__is_active=True)
    allarticle = Article.objects.filter(is_active=True).order_by('-id')
    alltag = Tag.objects.distinct().filter(article__is_active=True)
    tags = alltag

    return render(request, 'tags.html', locals())


# 标签详情页
def tag_info(request,tagId):
    allcategory = Category.objects.filter(article__is_active=True)
    allarticle = Article.objects.filter(is_active=True).order_by('-id')
    alltag = Tag.objects.distinct().filter(article__is_active=True)

    list = Article.objects.filter(tags__id=tagId, is_active=True) #获取通过URL传进来的lid，然后筛选出对应文章
    tag = Tag.objects.get(id=tagId)#获取当前标签
    list = page_list(request, list)

    return render(request, 'tag_info.html', locals())


# 内容页
def show(request, sid):
    allcategory = Category.objects.filter(article__is_active=True)
    allarticle = Article.objects.filter(is_active=True).order_by('-id')
    alltag = Tag.objects.distinct().filter(article__is_active=True)

    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    # markdown转html
    show.bodyhtml = markdown.markdown(show.body, extensions=[
       'markdown.extensions.extra',
       'markdown.extensions.codehilite',
       'markdown.extensions.toc',
    ])
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    next_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())


# 搜索页
def search(request):
    ss = request.GET.get('search')  # 获取搜索的关键词
    list = Article.objects.filter(title__icontains=ss, is_active=True)  # 获取到搜索关键词通过标题进行匹配
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    list = page_list(request, list)
    return render(request, 'search.html', locals())


def page_list(request, list):
    page = request.GET.get('page')
    if page is None:
        page = 1
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return list

# 关于我们
def about(request):
    allcategory = Category.objects.filter(article__is_active=True)
    allarticle = Article.objects.filter(is_active=True).order_by('-id')
    alltag = Tag.objects.distinct().filter(article__is_active=True)
    return render(request, 'about.html',locals())
