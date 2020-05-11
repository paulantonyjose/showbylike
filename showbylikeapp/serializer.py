from rest_framework import serializers

class FinalSerializer(serializers.Serializer):
	lst_images= serializers.ListField(child=serializers.CharField(max_length=100))
	txt_description = serializers.CharField(max_length=100)
	chr_status = serializers.CharField(max_length=7)
	int_likes =serializers.IntegerField()
	int_dislikes = serializers.IntegerField()
	id =serializers.IntegerField()
    #dat_created = serializers.Datefield()