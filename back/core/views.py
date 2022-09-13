from .serializers import *
from .models import *

from rest_framework import viewsets


class RatingViewSet(viewsets.ModelViewSet):

    serializer_class = RatingSerializer
    queryset = handbook.Rating.objects.all()


class DealTypeViewSet(viewsets.ModelViewSet):

    serializer_class = DealTypeSerializer
    queryset = handbook.DealType.objects.all()


class PlaceViewSet(viewsets.ModelViewSet):

    serializer_class = PlaceSerializer
    queryset = handbook.Place.objects.all()


class InventoryTypeViewSet(viewsets.ModelViewSet):

    serializer_class = InventorySerializer
    queryset = handbook.Inventory.objects.all()


class CounterpartyViewSet(viewsets.ModelViewSet):

    serializer_class = CounterpartySerializer
    queryset = objects.Counterparty.objects.all()


class DealViewSet(viewsets.ModelViewSet):

    serializer_class = DealSerializer
    queryset = objects.Deal.objects.all()