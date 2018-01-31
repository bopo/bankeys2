# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import TimelineViewSet, CommentViewSet, ReplyViewSet

router = DefaultRouter()
router.register(r'timeline', TimelineViewSet, base_name='timeline')
router.register(r'comment', CommentViewSet, base_name='comment')
router.register(r'reply', ReplyViewSet, base_name='reply')

urlpatterns = (
    url(r'', include(router.urls)),
)
