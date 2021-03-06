from django.contrib import admin
from .models import EnWord, RuWord, PartOfSpeech


class EnWordAdmin(admin.ModelAdmin):
    list_display = ['pk', 'word', 'get_translate', 'get_part_of_speech']
    search_fields = ['word']


class RuWordAdmin(admin.ModelAdmin):
    list_display = ['pk', 'word']
    search_fields = ['word']


class PartOfSpeechAdmin(admin.ModelAdmin):
    model = PartOfSpeech


admin.site.register(EnWord, EnWordAdmin)
admin.site.register(RuWord, RuWordAdmin)
admin.site.register(PartOfSpeech, PartOfSpeechAdmin)