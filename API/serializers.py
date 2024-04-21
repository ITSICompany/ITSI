from rest_framework import serializers
from ITSI_ID.models import Users

class AnaliticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','analytics')
        
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','name', 'surname', 'avatar', 'team', 'products', 'services', 'analytics')