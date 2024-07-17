from rest_framework import serializers
from a_work.models import Work

class WorkSerializer(serializers.ModelSerializer):
    is_bookmarked=serializers.SerializerMethodField()
    has_writer=serializers.SerializerMethodField()
    is_mine=serializers.SerializerMethodField()
    class Meta:
        model=Work
        fields=['id','work_code','deadline','words', 'type','created_at', 'is_bookmarked', 'has_writer','is_mine']

    def get_is_bookmarked(self, obj):
        user=self.context['request'].user
        return user in obj.bookmarked_by.all()

    def get_has_writer(self, obj):
        return obj.has_writer
    
    def get_is_mine(self, obj):
        user=self.context['request'].user
        return obj.writer==user
        