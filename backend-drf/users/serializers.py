from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User 
        fields = ['id','email','username','password']
        
    def Create(self, velidated_data):
        user = User.objects.create_user(**velidated_data)
    
        return User        