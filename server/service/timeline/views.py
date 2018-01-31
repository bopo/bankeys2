# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import mixins
from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from service.timeline.models import Timeline, Comment, Reply


class TimelineViewSet(NestedViewSetMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    permission_classes = (IsAuthenticated,)
    model = Timeline

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = self.queryset.filter(owner=self.request.user)

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        return queryset


class CommentViewSet(NestedViewSetMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    permission_classes = (IsAuthenticated,)
    model = Comment

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.request.user.comment_set.all()


class ReplyViewSet(NestedViewSetMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    permission_classes = (IsAuthenticated,)
    model = Reply

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.request.user.reply_set.all()
