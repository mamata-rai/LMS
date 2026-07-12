from library_app.models import  Category

def navigation_context(request):
    categories = Category.objects.all()[:3]
    categoriesall = Category.objects.all()

    return {
        "categories":categories,
        "categoriesall":categoriesall,
        # "random_posts": random_posts,

       

    }