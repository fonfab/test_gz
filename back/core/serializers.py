from rest_framework import serializers
from .models import *


class RatingSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    rating = serializers.CharField(max_length=10)

    class Meta:
        model = handbook.Rating
        fields = '__all__'

    def create(self, validated_data):
        return handbook.Rating.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance


class DealTypeSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    class Meta:
        model = handbook.DealType
        fields = '__all__'

    def create(self, validated_data):
        return handbook.DealType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class PlaceSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    class Meta:
        model = handbook.Place
        fields = '__all__'

    def create(self, validated_data):
        return handbook.Place.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class InventorySerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    class Meta:
        model = handbook.Inventory
        fields = '__all__'

    def create(self, validated_data):
        return handbook.Inventory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class CounterpartySerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    rating_id = serializers.IntegerField()
    rating = RatingSerializer(read_only=True)

    class Meta:
        model = objects.Counterparty
        fields = '__all__'

    def create(self, validated_data):
        return objects.Counterparty.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.rating_id = validated_data.get('rating_id', instance.rating_id)
        instance.save()
        return instance


class DealSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    type_id = serializers.IntegerField()
    type = DealTypeSerializer(read_only=True)

    deal_date = serializers.DateTimeField()

    destination_place_id = serializers.IntegerField()
    destination_place = PlaceSerializer(read_only=True)

    amount = serializers.FloatField()
    cost = serializers.FloatField()

    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()

    inventory_id = serializers.IntegerField()
    inventory = InventorySerializer(read_only=True)

    counterparty_id = serializers.IntegerField()
    counterparty = CounterpartySerializer(read_only=True)

    class Meta:
        model = objects.Deal
        fields = '__all__'

    def create(self, validated_data):
        return objects.Deal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.type_id = validated_data.get('type_id', instance.type_id)
        instance.deal_date = validated_data.get('deal_date', instance.deal_date)
        instance.destination_place_id = validated_data.get('destination_place_id', instance.destination_place_id)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.inventory_id = validated_data.get('inventory_id', instance.inventory_id)
        instance.counterparty_id = validated_data.get('counterparty_id', instance.counterparty_id)
        instance.save()
        return instance


class TestDealSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    type_id = serializers.IntegerField()
    type = DealTypeSerializer(read_only=True)

    deal_date = serializers.DateTimeField()

    destination_place_id = serializers.IntegerField()
    destination_place = PlaceSerializer(read_only=True)

    amount = serializers.FloatField()
    cost = serializers.FloatField()

    amount_new = serializers.FloatField()
    cost_new = serializers.FloatField()

    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()

    inventory_id = serializers.IntegerField()
    inventory = InventorySerializer(read_only=True)

    counterparty_id = serializers.IntegerField()
    counterparty = CounterpartySerializer(read_only=True)

    class Meta:
        model = objects.Deal
        fields = '__all__'

    def create(self, validated_data):
        return objects.Deal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.type_id = validated_data.get('type_id', instance.type_id)
        instance.deal_date = validated_data.get('deal_date', instance.deal_date)
        instance.destination_place_id = validated_data.get('destination_place_id', instance.destination_place_id)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.inventory_id = validated_data.get('inventory_id', instance.inventory_id)
        instance.counterparty_id = validated_data.get('counterparty_id', instance.counterparty_id)
        instance.save()
        return instance


class ReportSerializer(serializers.Serializer):

    rating_name = serializers.CharField(max_length=10)
    amount = serializers.FloatField()
    cost = serializers.FloatField()
