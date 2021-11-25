from django.contrib import admin
from .models import Project, Contributor


class ProjectAdmin(admin.ModelAdmin):
    pass    
    

class ContributorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor, ContributorAdmin)

