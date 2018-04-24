from django.contrib import admin

from fightgame.models import *

class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'finish_date', 'category']
    search_fields = ['name']
    list_filter = ['start_date', 'finish_date']

class FighterAdmin(admin.ModelAdmin):
    list_display = ['alias', 'skills', 'force', 'resistance']
    search_fields = ['alias']

class CombatAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'tournament', 'date', 'winner']
    search_fields = ['winner', 'loser']
    list_filter = ['tournament', 'date']

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Fighter, FighterAdmin)
admin.site.register(Combat, CombatAdmin)
