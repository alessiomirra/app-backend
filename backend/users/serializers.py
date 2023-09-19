from rest_framework import serializers 
from djoser.serializers import UserSerializer, UserCreateSerializer 
from users.models import CustomUser, Objective 

from datetime import date 

############ 

class CustomUserSerializer(UserSerializer):
    heightM = serializers.SerializerMethodField(read_only=True)
    age = serializers.SerializerMethodField(read_only=True)

    class Meta(UserSerializer.Meta): 
        model = CustomUser 
        fields = "__all__"

    def get_heightM(self, instance):
        if instance.height:
            return instance.height / 100  
        return None 

    def get_age(self, instance):
        if instance.born:
            today = date.today()
            born = instance.born
            age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            return age
        return None 

class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ["username","email","password","weight","height","born"] 

    
class ObjectiveSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    created = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Objective
        fields = "__all__"

    def get_created(self, instance):
        return instance.created.strftime('%d %B %Y')
