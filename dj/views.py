from django.shortcuts import render,redirect,reverse
from dj import models
# Create your views here.
def book_list(request):
    all_books = models.Book.objects.all()

    return render(request, "book_list.html", {"all_books":all_books})


def add_book(request):
    if request.method =="GET":
        return render(request,"add_book.html")
    else:
        id = request.POST.get('book_id')
        title = request.POST.get('book_name')
        price = request.POST.get('book_price')
        publish = request.POST.get('book_pub')
        models.Book.objects.create(id=id,title=title,price=price,publish=publish)
    return redirect(reverse("book_list"))