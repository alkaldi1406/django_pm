from django.contrib import admin
from django.db.models import Count

from . import models

# Register your models here.

admin.site.register(models.Category)

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','user','category','created_at','tasks_count')
    list_per_page = 20
    list_select_related = ('category','user')# لمنع الاستعلامات الكثيرة
    list_editable = ['status']#لتحديد الاعمدة القابلة لتعديل ويمكن اضافة اي عمود اخر للقائمة هنا



    def get_queryset(self, request):
        # نقوم بإضافة عمod "وهمي" اسمه tasks__count يحتوي على العدد مسبقاً
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(tasks_count=Count('task'))
        return queryset

        # الآن الدالة لا تنفذ استعلاماً، بل تقرأ القيمة الجاهزة فقط

    def tasks_count(self, obj):
        return obj.tasks_count



@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description','project','is_completed')
    list_per_page = 20
    list_editable = ['is_completed']





