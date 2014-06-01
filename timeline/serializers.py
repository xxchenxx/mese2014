from rest_framework import serializers

class	TimelineSerializer(serializers.Serializer):

	year = serializers.IntegerField()
	quarter = serializers.IntegerField(default = 1)
	
