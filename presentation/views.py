from django.shortcuts import render
from gallery.models import Gallery


def home(request):
	# gallerys = Gallery.description 把model的描述传递给这个变量
	gallerys = Gallery.objects #其实model中的描述可能有多个，所以应该传递整个对象给变量再用循环输出在html中
	return render(request,'home.html',{'gallerys':gallerys})
