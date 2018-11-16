from django.contrib import admin

# Register your models here.

#Import Your Model
from collection.models import Jersey

#Set Up Automated Slug Creation
class JerseyAdmin(admin.ModelAdmin):
    model = Jersey
    list_display = ('name', 'description',) #Tells Django that we want this to show in admin
    prepopulated_fields = {'slug': ('name',)} #Prepopulate the slug field based off of the name field when someone types the name of a jersey in the admin

#Register Your Model
admin.site.register(Jersey, JerseyAdmin)