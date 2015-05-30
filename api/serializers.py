from rest_framework import serializers
from broadcasts.models import Slide, Broadcasting, Event

class SlidePostSerializer(serializers.ModelSerializer):
    file = serializers.ImageField()
    broadcasting = serializers.PrimaryKeyRelatedField(queryset=Broadcasting.objects.all())
    
    class Meta:
        model = Slide
        fields = ('file', 'broadcasting', 'dt_create')
        
class SlideGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = ('file', 'broadcasting', 'position', 'dt_upload')
        
class BroadcastingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broadcasting
        fields = ('title', 'owner', 'active')