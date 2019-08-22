from django.contrib import admin
from .models import Gallery #这样才是导入同级文件

# Register your models here.
admin.site.register(Gallery) #括号里面是model的名字