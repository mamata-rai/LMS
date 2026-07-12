from django.contrib import admin

from .models import  Book,Student,IssueBook,Fine,Teacher,Category
# Register your models here.
admin.site.register(Book)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(IssueBook)
admin.site.register(Fine)






