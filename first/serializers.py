from rest_framework import serializers
from .models import Car
from django.contrib.auth.models import User
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"




    def validate_country(self, value):
# Пример валидации поля "country"
        valid_countries = ["Korea", "Germany", "Japan"]
        if value not in valid_countries:
            raise serializers.ValidationError
            ("Недопустимая страна производства.")
        return value

    def validate_name(self, value):
# Пример валидации поля "country"
        valid_names = ["BMW X5", "Hyundai Sonata", "Toyota Camry"]
        if value not in valid_names:
            raise serializers.ValidationError
            ("Недопустимое название авто.")
        return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')