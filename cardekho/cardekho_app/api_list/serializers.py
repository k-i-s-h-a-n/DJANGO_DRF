from rest_framework import serializers
from ..models import carList



def alphanumeric(value):
    if not value.isalnum():
        raise serializers.ValidationError("Only alphanumeric characters are allowed.")
    return value

class carSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description=serializers.CharField()
    active = serializers.BooleanField(read_only=False)
    chasisNumber = serializers.CharField(validators=[alphanumeric])
    price = serializers.DecimalField(max_digits=10, decimal_places=2,)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return carList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.chasisNumber = validated_data.get('chasisNumber', instance.chasis)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
    
    def validate_price(self, value):
        if value <=20000.00:
            raise serializers.ValidationError("Price must be greater than 20000.")
        return value

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Price and description cannot be same.")
        return data