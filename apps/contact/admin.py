from django.contrib import admin
from .models import Contact, FAQ, Answer, Feedback


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    inlines = (AnswerInline, )
    list_display = ('id', 'question')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number')


@admin.register(Feedback)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'rate')