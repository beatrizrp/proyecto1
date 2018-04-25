from rest_framework import serializers

from .models import *


class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tournament
        fields = ('id','name', 'start_date', 'finish_date', 'category')

class CombatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Combat
        fields = ('id','tournament','date', 'loser', 'winner')

class FighterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fighter
        fields = ('id','alias', 'skills', 'force', 'resistance', 'gender')