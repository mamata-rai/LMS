from library_app.models import  Category

def navigation_context(request):
    categories = Category.objects.all()[:3]
    categoriesall = Category.objects.all()

    # tags = Tag.objects.all()[:4]
    # trending_posts = Post.objects.filter(
    #     published_at__isnull = False, status ="active"
    #     ).order_by("-view_count")[:3]
    # random_posts = Post.objects.filter(published_at__isnull=False, status="active" , featured_image__isnull=False).order_by("?")[:6]
    
    return {
        "categories":categories,
        "categoriesall":categoriesall,
        # "random_posts": random_posts,

       

    }