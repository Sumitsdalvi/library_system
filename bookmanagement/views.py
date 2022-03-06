from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Books
# import logging
# Create your views here.
# http://127.0.0.1:8000/home
# log_file_path = r"E:\PythonPractice\Django_work\library_system\Library_log.log"

def homepage(request):
    # print("Request method in home page is :- ")
    # print(request.POST)
    # if request.POST["is_active"] == 'on':
    #     book_status = 0
    # else:
    #     book_status = 1
    # print(type(request.POST["bname"]))
    if request.method == "POST":
        if not request.POST.get("bid"):
            book_name = request.POST["bname"]
            book_price = request.POST["bprice"]
            book_qty = request.POST["bqty"]
            book_status = request.POST["is_active"]
            try:
                Books.objects.create(name = book_name , price = book_price , qty = book_qty, is_active = book_status)
            except ValueError as Err_msg:
                print(Err_msg)
                return HttpResponse("One or more values that you have entered is/are not valid!!")
            return redirect("homepage")
        else:
            bid = request.POST.get("bid")
            book_obj = Books.objects.get(id=bid)
            book_obj.name = request.POST["bname"].replace("-"," ")
            book_obj.price = request.POST["bprice"]
            book_obj.qty = request.POST["bqty"]
            book_obj.is_active = request.POST["is_active"]
            book_obj.save()
            return redirect("show_all_books")
    elif request.method == "GET":
        return render(request,template_name="Home.html")
# def submit_form(request):
#     pass

def show_all_books(request):
    allbooks = Books.objects.all() 
    return render(request , "show-all-books.html" , {"books" : allbooks} )

def show_active_books(request):
    try:
        activebooks = Books.act_books.all()  # This is custom model manager
    except Books.DoesNotExist as err_msg:
        return HttpResponse("No Book is in active state...!!!")
    else:
        return render(request , "show-all-books.html" , {"books" : activebooks} )

def show_inactive_books(request):
    try:
        inactivebooks = Books.inactive_books.all()  # This is custom model manager
    except Books.DoesNotExist as err_msg:
        return HttpResponse("No Book is in inactive state...!!!")
    else:   
        return render(request , "show-all-books.html" , {"books" : inactivebooks} )


def edit_data(request,id):
    try:
        req_book = Books.objects.get(id=id)
    except Books.DoesNotExist as err_msg:
        return HttpResponse(f"Book hvaing ID :- {id} which you are trying to edit is not avaailable in Library..!!")
    return render(request,template_name="Home.html", context = {"required_book" : req_book})

def delete_book(request,id):
    if request.method == "POST":
        try:
            req_book = Books.objects.get(id=id)
        except Books.DoesNotExist as err_msg:
            return HttpResponse(f"Book hvaing ID :- {id} which you are trying to delete is not avaailable in Library..!!")
        else:
            req_book.delete()
            return redirect("show_all_books")
    else:
        return HttpResponse("Prohibited:- You are trying to delete directly by using URL...!!!")

def soft_delete_book(request,id):
    if request.method == "POST":
        try:
            req_book = Books.objects.get(id=id)
        except Books.DoesNotExist as err_msg:
            return HttpResponse(f"Book hvaing ID :- {id} which you are trying to delete is not avaailable in Library..!!")
        else:
            if req_book.is_active:
                req_book.is_active = False
            else:
                req_book.is_active = True
            req_book.save()
            return redirect("show_all_books")
    else:
        return HttpResponse("Prohibited:- You are trying to delete directly by using URL...!!!")