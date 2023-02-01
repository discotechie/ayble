from rest_framework import serializers
from users.models import CustomUser
from health.serializers import SymptomSerializer, DiagnosisSerializer, FoodSerializer
from rest_framework.fields import CurrentUserDefault

class UserList(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'email', 'is_staff', 'date_of_birth', 'sex_at_birth']

class UserDetail(serializers.ModelSerializer):

    symptoms = SymptomSerializer(many=True, read_only=True)
    diagnoses = DiagnosisSerializer(many=True, read_only=True)
    trigger_foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['url', 'email', 'is_staff', 'date_of_birth', 'sex_at_birth', 'symptoms', 'diagnoses', 'trigger_foods']