from django.contrib import admin
from .models import *
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# Register your models here.


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class UserQueryAdmin(admin.ModelAdmin):
    list_display = ('userID', 'timestamp', 'messageBody')
    ordering = ('-timestamp',)

    def upload_csv(self, request):
        if request.method == 'POST':
            csv_file = request.FILES("csv_upload")

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = UserQuery.objects.update_or_create(
                    userID = fields[0],
                    timestamp = fields[1],
                    messageBody = fields[2]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(UserQuery, UserQueryAdmin)