from django.contrib import admin
from .models import railway
from .forms import railwayForm


# 自定义表单管理
class railwayAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'leave_city', 'arrive_city', 'leave_station', 'arrive_station', 'leave_time', 'arrive_time', 'capacity',
        'price', 'book_sum', 'income')
    form = railwayForm  # 在railwayForm中自定义需要在后台中输入哪些信息

# Register your models here.
admin.site.register(railway, railwayAdmin)
