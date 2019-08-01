from django.contrib import admin

from .models import Choice,Question,Profile,Publication,Article

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ('pub_date', 'question_text',)


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.question_text, obj.was_published_recently)).upper()
    upper_case_name.short_description = 'Name'
    list_display = ('question_text','pub_date','was_published_recently','upper_case_name')
    list_filter = ['pub_date']
    search_fields = ('question_text',)

admin.site.register(Question, QuestionAdmin)



admin.site.register(Choice)
admin.site.register(Profile)

admin.site.register(Publication)
admin.site.register(Article)
