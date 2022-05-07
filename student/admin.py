from django.contrib import admin
from django.utils.html import format_html

from student.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'age')

    def full_name(self, instance):
        if instance.social_url is not None:
            return format_html(f'<a href="{instance.social_url}"> {instance.first_name} {instance.last_name}</a>')
        return f'{instance.first_name} {instance.last_name}'


admin.site.register(Person, PersonAdmin)
