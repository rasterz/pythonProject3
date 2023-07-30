from django.contrib import admin

from goals.models import GoalComment, Goal, GoalCategory


# Register your models here.

@admin.register(GoalCategory)
class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_deleted',)
    readonly_fields = ('created', 'updated',)
    list_filter = ('is_deleted',)
    search_fields = ('title',)


@admin.register(Goal)
class GoalAdmin (admin. ModelAdmin):
    list_display = ('id', 'title', 'user', 'category')
    search_fields = ('title', 'description')
    readonly_fields = ('created', 'updated',)
    list_filter = ('status', 'priority')



