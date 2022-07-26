from django.contrib import admin
from .models import Post

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_modified', 'status')
    '''
    این پایینیا رو خودم اضافه کردم. لیست دیسپلی لینکس، یه لیست یا تاپل بهش
    میدیم و آیتم هایی که میذاریم به لینک تبدیل میشن و با کلیک روشون
    ما رو میبره به صفحه ویرایششون.
    لیست ادیتبل هم باید چیزایی رو بذاریم که به صورت کمبوباکس باشن و بشه
    همونجا راحت عوضشون کرد. مثلا استاتوس یا نویسنده که کمبوباکس داشتن
    جفتشون. ولی تایتیل یا تاریخ رو گذاشتم ارور میداد و نمیشد گذاشت.
    قاعدتا چیزایی هم که میذاریم باید توی لیست دیسپلیمون باشن که بشه
    تو بعدی ها هم گذاشتشون.
    '''
    # list_display_links = ('title', 'date_modified', ) 
    # list_editable = ('status', 'author', )

admin.site.register(Post, PostAdmin)