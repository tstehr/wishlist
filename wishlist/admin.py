from django.contrib import admin

from .models import Wish


class WishAdmin(admin.ModelAdmin):
    fields = ['title_text', 'description_text', 'importance']


admin.site.register(Wish, WishAdmin)