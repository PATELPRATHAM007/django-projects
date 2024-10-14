from django.shortcuts import render,get_object_or_404
from .models import Book
from django.db.models import Avg, Max , Min,Count

# Create your views here.
def index(request):
    books = Book.objects.all()
    # books = Book.objects.all().order_by("rating")
    # books = Book.objects.all().order_by("-rating")
    total_book = books.count()
    avg_book_rating = books.aggregate(Avg("rating"))

    return render(request,"book_outlet/index.html",{
        "books" : books,
        "totalBooks" : total_book,
        "averageRating" : avg_book_rating
    })


def book_details(request,slug):
    book = get_object_or_404(Book,slug=slug)
    return render(request, 'book_outlet/book_details.html', {'book': book})