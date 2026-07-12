from django.contrib import admin

from .models import  Book,Student,IssueBook,Fine,Teacher,Category
# Register your models here.
admin.site.register(Book)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(IssueBook)
admin.site.register(Fine)



# from news_app.models import Post, Category, Tag, Contact, userprofile,Comments, Newsletter

# # Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)
# admin.site.register(Tag)
# admin.site.register(Contact)
# admin.site.register(userprofile)
# admin.site.register(Comments)
# admin.site.register(Newsletter)





