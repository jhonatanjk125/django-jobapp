from django.contrib import admin
from app.models import Author, JobPost, Location, Skill

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'date', 'expires_on')
    list_filter = ('date','salary','expires_on')
    search_fields = ('title',)
    search_help_text = "Write a job title and hit enter"
    # fields = (('title', 'description'), 'expires_on')
    fieldsets = (('Basic information',
                  {'fields':('title','description')}),
                  ('Detailed information',
                  {'classes':('collapse',),
                   'fields':(('salary','expires_on'),'slug')}),
                  )
# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skill)
