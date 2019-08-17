from django.contrib import admin
from .models import  Subreddit, SubredditMembers


class SubredditMembersInline(admin.TabularInline):
    model = SubredditMembers


admin.site.register(Subreddit)
admin.site.register(SubredditMembers)
