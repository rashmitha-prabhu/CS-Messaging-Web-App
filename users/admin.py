from django.contrib import admin
from .models import *
from django.shortcuts import render
from django.utils.html import format_html
from django.urls import re_path


# Register your models here.


@admin.register(UserQuery)
class UserQueryAdmin(admin.ModelAdmin):
    list_display = ('userID', 'timestamp', 'messageBody', 'urgency_status', 'resolved', 'action')
    ordering = ('urgency_status', '-timestamp',)
    list_per_page = 20
    search_fields = ['userID', 'messageBody', 'urgency_status']
    list_filter = ['urgency_status', 'resolved']


    def action(self, obj):
        if not obj.resolved:
            obj.resolved = True
            return format_html(f'<a href="/user/userquery/{obj.id}/resolve">Resolve</a>')
        else:
            obj.resolved = False
            return format_html(f'<a href="/user/userquery/{obj.id}/unresolve">Unresolve</a>')
