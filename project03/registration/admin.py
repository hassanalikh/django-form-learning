from django.contrib import admin
from .models import Students
# Register your models here.

# Register the modal class by DECORATOR


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('stuid', 'name', 'program', 'city',)


# register the multiple classes

# admin.site.register(Students, StudentsAdmin)
