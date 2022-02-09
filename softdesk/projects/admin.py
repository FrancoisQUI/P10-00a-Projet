from django.forms import ModelForm, SelectMultiple
from django.contrib import admin
from .models import Project, Contributor


class ProjectAdmin(admin.ModelAdmin):
    pass    
    

class ContributorAdminForm(ModelForm):
    class Meta:
        model = Contributor
        widgets = {
            'permission': SelectMultiple
        }
        fields = '__all__'


class ContributorAdmin(admin.ModelAdmin):
    form = ContributorAdminForm


admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor, ContributorAdmin)
