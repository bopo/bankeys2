# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from service.kernel.models.consumption import Contract
from service.kernel.serializers.consumption import ConsumptionSerializer


class ContractViewSet(viewsets.ModelViewSet):
    '''
    合约接口
    ----

    合约类型
    ('receipt', '收据'),
    ('borrow', '借条'),
    ('owe', '欠条'),


    '''
    queryset = Contract.objects.all()
    serializer_class = ConsumptionSerializer
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('POST', 'OPTION', 'HEAD')

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def get_queryset(self):
        queryset = self.queryset.filter(sender=self.request.user)

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        return queryset
