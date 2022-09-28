from .serializers import *
from .models import *

from rest_framework import viewsets, views, response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum, F, ExpressionWrapper, IntegerField

from utils.exchange_rate import get_exchange_rate


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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['counterparty_id', ]


class ReportView(viewsets.ViewSet):

    def list(self, request):
        rate = get_exchange_rate()

        items = objects.Deal.objects.annotate(
            duration=ExpressionWrapper(F('end_date') - F('start_date'), output_field=IntegerField()),
            duration_hours=F('duration') / 60 / 60 / 1000000,
            amount_new=F('amount') * F('duration_hours') / 10.4,
            cost_new=F('cost') * 10.4 * rate,
            rating_name=F('counterparty__rating__rating')
        ).values(
            'rating_name',
        ).annotate(
            amount=Sum('amount_new'),
            cost=Sum('cost_new'),
        ).all()

        serializer = ReportSerializer(items, many=True)
        return response.Response(serializer.data)
