from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    search_fields = ('text',)
    date_hierarchy = 'date_posted'
    list_filter = ('date_posted',)
    list_editable = ('text',)
    fields = ('text', )

    # @admin.display(description="Title")
    # def upper_title(self, obj):
    #     return f"{obj.id} - {obj.text}".upper()


admin.site.register(Comment, CommentAdmin)


