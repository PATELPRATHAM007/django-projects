from django.shortcuts import render,get_object_or_404
from .models import Book
# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request,"book_outlet/index.html",{
        "books" : books
    })


def book_details(request,id):
    book = get_object_or_404(Book,pk=id)
    return render(request, 'book_outlet/book_details.html', {'book': book})