# coding:utf-8
from __future__ import unicode_literals

from django.db import models


# usb 签名数据表

class Usb(models.Model):
    req_id = models.CharField(verbose_name='reqID', max_length=100, unique=True)
    sin_data = models.TextField(verbose_name='签名数据')

    def __unicode__(self):
        return '%s' % (self.sin_data,)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = (u'u盾签名数据')
        verbose_name_plural = (u'u盾签名数据')

    def save(self, *args, **kwargs):
        import hashlib

        m = hashlib.md5()
        m.update(self.sin_data)
        self.req_id = m.hexdigest()

        return super(Usb, self).save()
