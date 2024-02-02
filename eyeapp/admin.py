from django.contrib import admin
from .models import Category, Icon, Service, Doctor, DoctorDetails, ServiceDetails, CategoryDetails, Gallery, Mizhi, Equipment, Blog, BlogCategory, Review, ManagementTeam, ManagementTeamDetails


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'featured', 'service_nav')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('featured', 'service_nav')
    list_filter = ('featured', 'service_nav')
    search_fields = ('name', 'description')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'role']
    prepopulated_fields = {'slug': ('name',)}


class IconAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured')
    list_editable = ('featured', 'category')
    prepopulated_fields = {'slug': ('title',)}


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'what_doctor', 'doctor_name',)


class ManagementTeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'role']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryDetails)
admin.site.register(Icon, IconAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceDetails)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(DoctorDetails)
admin.site.register(Gallery)
admin.site.register(Mizhi)
admin.site.register(Equipment)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogCategory)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ManagementTeam, ManagementTeamAdmin)
admin.site.register(ManagementTeamDetails)
