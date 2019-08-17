from django.contrib import admin
from .models import Subreddit, SubredditMembers


class SubredditMembersInline(admin.TabularInline):
    model = SubredditMembers


class SubredditAdmin(admin.ModelAdmin):
    inlines = [
        SubredditMembersInline,
    ]


admin.site.register(Subreddit, SubredditAdmin)
admin.site.register(SubredditMembers)
