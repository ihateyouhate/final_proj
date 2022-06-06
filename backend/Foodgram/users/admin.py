from django.contrib import admin

from .models import Follow, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
    list_filter = ('username', 'email')
    search_fields = ('username', 'email')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'following')


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
