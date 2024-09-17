from django.shortcuts import render
from django.shortcuts import render,HttpResponse

# Create your views here.

#1.查询字符串
def book_detail_query_string(request):
    #request.GET = {"id",3}
    book_id = request.GET.get('id')
    book_name = request.GET.get("name")
    return HttpResponse(f"您查找的图书id是：{book_id}，名字是{book_name}")

def book_detail_path(request,book_id):
    return HttpResponse(f"您查找的图书id是：{book_id}")


