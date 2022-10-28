from pydoc import resolve
from tokenize import Triple
from django.contrib import admin
from .models import *
from django.contrib import admin

# Register your models here.


class UserQueryAdmin(admin.ModelAdmin):
    list_display = ('userID', 'timestamp', 'messageBody', 'urgency_status', 'resolved')
    ordering = ('userID', '-timestamp',)
    list_per_page = 20
    search_fields = ['userID', 'messageBody', 'urgency_status']
    actions = ['resolve', 'unresolve']
    list_filter = ['urgency_status', 'resolved']

    def resolve(self, request, queryset):
        queryset.update(resolved=True)

    def unresolve(self, request, queryset):
        queryset.update(resolved=False)


admin.site.register(UserQuery, UserQueryAdmin)