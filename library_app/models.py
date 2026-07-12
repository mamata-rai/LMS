# from django.db import models
# from django.core.validators import FileExtensionValidator
# from django.utils import timezone
# from django.contrib.auth.models import User
# from datetime import datetime

# import django.utils.timezone
# django.utils.timezone.now

# # Create your models here.

# class TimeStampModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         abstract = True

# class Category(TimeStampModel):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name



# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author =models.CharField(max_length=255)
#     is_availible = models.BooleanField(default=True)
#     Category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True,blank=True)
#     image = models.ImageField(upload_to='book_images/', blank=False)
#     published_at = models.DateTimeField(null=True,blank=True)
#     view_count=models.PositiveBigIntegerField(default=0)

#     pdf_file = models.FileField(
#         upload_to='book_pdfs/',null=True,blank=True)

#     def __str__(self):
#         return self.title

# class Teacher(models.Model):
#     name = models.CharField(max_length=100)
#     subject = models.CharField(max_length=50)
#     email = models.EmailField()

# class Student(models.Model):
#     name =models.CharField(max_length=100)
#     roll_no=models.CharField(max_length=20,unique=True)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)

# class IssueBook(TimeStampModel):
#     student = models.ForeignKey(Student,on_delete=models.CASCADE)
#     book=models.ForeignKey(Book,on_delete=models.CASCADE)
#     issue_date =models.DateField()
#     return_date=models.DateField()

# class Fine(models.Model):
#     issue = models.OneToOneField(IssueBook,on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=6,decimal_places=2)




# # Create your models here.


# class BorrowRecord(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     book = models.ForeignKey(Book,on_delete=models.CASCADE)
#     borrow_date = models.DateField(default=datetime.now)
#     return_date =  models.DateField(null=True,blank=True)

#     def __str__(self):
#         return f"{self.user.username} borrowed {self.book.title}"
    







from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from datetime import datetime
from django.utils import timezone

# # # Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




class Category(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    is_available = models.BooleanField(default=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    image = models.ImageField(upload_to='book_images/')
    published_at = models.DateTimeField(null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)

    pdf_file = models.FileField(
        upload_to='book_pdfs/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title



class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name




class IssueBook(TimeStampModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.book.title}"




class Fine(models.Model):
    issue = models.OneToOneField(IssueBook, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    paid = models.BooleanField(default=False)

    # def __str__(self):
    #     return f"{self.amount}"




class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    borrow_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} → {self.book.title}"