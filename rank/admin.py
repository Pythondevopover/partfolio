from django.contrib import admin
from .models import UserRank

@admin.register(UserRank)
class UserRankAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'rank')  # Admin panelda ko'rinadigan ustunlar