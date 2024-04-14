from django.contrib import admin
from USMAApp.models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
class MyUserAdmin(BaseUserAdmin):
    list_display=('username', 'email', 'company_name', 'date_joined', 'last_login', 'is_admin', 'is_active')
    search_fields=('email', 'first_name', 'last_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'username', 'first_name', 'middle_name', 'last_name', 'company_name', 'phone', 'password1', 'password2'),
        }),
    )

    ordering=('email',)



class UniversitiesAdmin(admin.ModelAdmin):

	list_display = ["id", "UniversityName","UniversityPlace","Created","Updated"]
	list_filter =["Created","Updated"]
	search_fields = ["UniversityName"]

class UniversityCoursesAdmin(admin.ModelAdmin):

	list_display = ["id", "CourseName","CourseDepartment","CourseCapacity","Created","Updated"]
	list_filter =["Created","Updated"]
	search_fields = ["CourseName"]

class UdsmUniversityCoursesAdmin(admin.ModelAdmin):

	list_display = ["CourseName","CourseDepartment","CourseCapacity","Created","Updated"]
	list_filter =["Created","Updated"]
	search_fields = ["CourseName"]

class UdomUniversityCoursesAdmin(admin.ModelAdmin):

	list_display = ["CourseName","CourseDepartment","CourseCapacity","Created","Updated"]
	list_filter =["Created","Updated"]
	search_fields = ["CourseName"]

class MustUniversityCoursesAdmin(admin.ModelAdmin):

	list_display = ["CourseName","CourseDepartment","CourseCapacity","Created","Updated"]
	list_filter =["Created","Updated"]
	search_fields = ["CourseName"]

class DitUniversityCoursesAdmin(admin.ModelAdmin):

	list_display = ["CourseName","CourseDepartment","CourseCapacity","Created","Updated"]
	list_filter =["Created","Updated"]
	search_fields = ["CourseName"]


class ModulesAdmin(admin.ModelAdmin):

	list_display = ["ModuleName","course","Created","Updated"]
	list_filter =["Created","Updated"]
	search_fields = ["ModuleName"]

class StudentsAdmin(admin.ModelAdmin):

	list_display = ["FirstName","LastName","Email","Phone","course","Created","Updated"]
	list_filter =["Created","Updated"]
	search_fields = ["FirstName","LastName","Email","Phone"]

class TeachersAdmin(admin.ModelAdmin):

	list_display = ["FirstName","LastName","Email","Phone","Created","Updated"]
	list_filter =["Created","Updated"]
	search_fields = ["FirstName","LastName","Email","Phone"]


class AllProjectsAdmin(admin.ModelAdmin):

	list_display = ["ProjectName","StudentName","university","CourseName","Year","Gender","Created","Updated"]
	list_filter =["Created","Updated"]
	search_fields = ["ProjectName","StudentName","university","CourseName"]


class ArticlesAdmin(admin.ModelAdmin):

	list_display = ["ArticlesName","ArticleImage","Created","Updated"]
	list_filter =["Created","Updated"]
	search_fields = ["ArticlesName"]
class ArticlesCategoryAdmin(admin.ModelAdmin):

	list_display = ["Title","ArticlesName","WrittenBy","Github","Youtube","Created","Updated"]
	list_filter =["Created","Updated"]
	search_fields = ["Title"]







class HobAdmin(admin.ModelAdmin):

	list_display = ["CategoryName","Created","Updated"]
	list_filter =["Created","Updated"]
	search_fields = ["CategoryName"]

class ExpertsAdmin(admin.ModelAdmin):

	list_display = ["StudentName","CategoryName","StudentPlace","Phone","Created","Updated"]
	list_filter =["Created","Updated"]
	search_fields = ["StudentName"]


class ContactMeAdmin(admin.ModelAdmin):
    list_display = ["FullName", "Email", "Place","Phone","send_date"]
    #form = StockCreateForm
    #list_filter =['category']
    search_fields = ['FullName', 'Email']


admin.site.register(ContactMe, ContactMeAdmin)

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Universities, UniversitiesAdmin)

admin.site.register(UniversityCourses, UniversityCoursesAdmin)

admin.site.register(UdsmUniversityCourses,UdsmUniversityCoursesAdmin)
admin.site.register(UdomUniversityCourses, UdomUniversityCoursesAdmin)
admin.site.register(MustUniversityCourses, MustUniversityCoursesAdmin)
admin.site.register(DitUniversityCourses, DitUniversityCoursesAdmin)


admin.site.register(Modules, ModulesAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(AllProjects, AllProjectsAdmin)

admin.site.register(Articles, ArticlesAdmin)


admin.site.register(ArticlesCategory, ArticlesCategoryAdmin)
admin.site.register(Hob, HobAdmin)

admin.site.register(Experts, ExpertsAdmin)


