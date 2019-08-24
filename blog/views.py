from django.shortcuts import render
from .models import Blog 
# Create your views here.

def blog_page(request):
	blogs = Blog.objects
	return render(request,'blog.html',{'blogs':blogs})

# 从本级的models.py文件中导入Blog的model，再将导入的Blog的
#所有对象赋予给blog变量，这个变量再通过字典传递到html文件，再使用