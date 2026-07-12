# from library_app.models import Category

from django.shortcuts import redirect,render,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, CreateView, View, ListView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.utils import timezone

from .models import Book, BorrowRecord, Category,Fine,IssueBook,Student

# def home(request):

# class HomeView(TemplateView):
#     template_name = 'home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         books = Book.objects.all()

#         context['books'] = books
#         context['total_books'] = books.count()
#         context['available_books'] = books.filter(is_available=True).count()
#         return context
from .models import Book, Category
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()
        category_id = self.request.GET.get("category")
        if category_id:
            books = Book.objects.filter(category_id=category_id)
        else:
            books = Book.objects.all()

        paginator = Paginator(books, 3)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context["page_obj"] = page_obj
        context["books"] = books
        context["categories"] = categories
        context["total_books"] = books.count()
        context["available_books"] = books.filter(is_available=True).count()


        return context

# class Post(TimeStampModel):
#     STATUS_CHOICE = [
#         ("active","Active"),
#         ("in_active","Inactive"),
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     context["featured_post"] = Post.objects.filter(
    #         published_at__isnull = False, status ="active"
    #     ).order_by("-view_count", "-published_at").first()

    #     context["featured_posts"] = Post.objects.filter(
    #         published_at__isnull = False, status ="active"
    #     ).order_by("-view_count", "-published_at")[1:4]
        
    #     context["featured_post_right"] = Post.objects.filter(
    #         published_at__isnull = False, status ="active"
    #     ).order_by("-view_count", "-published_at")[4:10]

    #     one_week_ago = timezone.now() - timedelta(days=7)
    #     context["weekly_top_posts"] = Post.objects.filter(
    #         published_at__isnull = False, status ="active", published_at__gte=one_week_ago
    #     ).order_by("-view_count", "-published_at")[:7]
        
    #     context["recent_posts"] = Post.objects.filter(
    #         published_at__isnull = False, status ="active",
    #     ).order_by("-published_at")[:5]

        
        # return context
    
        # return context
    
class BorrowBookView(LoginRequiredMixin, View):
    def get(self, request, book_id):
    # GET request आएमा Home मा फर्काउने
        return redirect("home")

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        if not book.is_available:
            return redirect("home")
        
        student = Student.objects.filter(user=request.user).first()
      
        if not student:
            messages.error(request, "Student profile not found.")
            return redirect("home")
        IssueBook.objects.create(
            student=student,
            book=book,
            issue_date=timezone.now().date()
        )
        book.is_available = False

        book.save()
        messages.success(request, "Book borrowed successfully!")
        return redirect("my_books")
    
    
class ReturnBookView(LoginRequiredMixin, View):
    def get(self, request, issue_id):

        issue = get_object_or_404(IssueBook, id=issue_id)
        if issue.return_date:
            return redirect("home")
        issue.return_date=timezone.now().date()
        issue.save()
        days = (issue.return_date - issue.issue_date).days
        book = issue.book 
        book.is_available=True
        book.save()

        if days >30:
            Fine.objects.get_or_create( issue = issue, defaults={"amount":(days-30)*10})
        return redirect('home')
    
class MyBooksView(LoginRequiredMixin, ListView):
    model = IssueBook
    template_name = 'my_books.html'
    context_object_name = 'records'

    def get_queryset(self):
        student = Student.objects.filter(user=self.request.user).first()
        if student:
            return IssueBook.objects.filter(student=student,return_date__isnull=True)
        return IssueBook.objects.none()
class AddBookView(UserPassesTestMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'category', 'image', 'pdf_file']
    template_name = 'add_book.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_staff

class DeleteBookView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect("home")

    def test_func(self):
        return self.request.user.is_staff



class SignupView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'signup.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')


class PostByCategory(ListView):
    model = Book
    template_name = "library_app/category.html"
    context_object_name ="book"
    paginate_by = 1

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(
            published_at__isnull=False, status= "active",
            category__id = self.kwargs["category_id"],
        ).order_by(
            '-published_at',
        )
        return query


class CategoryBooksView(ListView):
    model = Book
    template_name = "category_books.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.filter(category_id=self.kwargs["id"])
    


# class MembershipView(TemplateView):
#     template_name = "footer/membership.html"
#     login_url = "login"

#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             messages.warning(request, "Please login to get membership.")
#             return redirect("login")
#         return super().dispatch(request, *args, **kwargs)  

class MembershipView(TemplateView):
    template_name = "footer/membership.html"
    login_url = "login"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, "Please login to get membership.")
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        messages.success(
            request,
            " Membership successful! Welcome to our team."
        )
        return redirect("home")


class AboutView(TemplateView):
    template_name="footer/about.html"


class ContactView(LoginRequiredMixin, TemplateView):
    template_name = "footer/contact.html"
    login_url="/"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, "Please login to contact us.")
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        if not name or not email or not message:
            messages.error(request,"Please fill all the fields")
            return redirect("contact")
        messages.success(request,"Message sent successfully")
        return redirect("/")

# class LoginView(TemplateView):
#     template_name="registration/login.html"