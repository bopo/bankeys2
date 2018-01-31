# -*- coding: utf-8 -*-
import requests

from service.kernel.contrib.utils import json
from service.kernel.models import Usb
from .test_base import BaseAPITestCase

# 验签地址
VERIFY_GATEWAY = 'http://10.7.7.22:9090'


class APITestusb(BaseAPITestCase):
    def setUp(self):
        self.init()

    # def test_req_usb(self):
    #     # 模拟数据
    #     a = "sddfdfdgdxsaasdsdad"
    #
    #     resp = requests.post(VERIFY_GATEWAY + '/Sign', data=a)
    #     print resp.content
    #     r = self.get('/api/usb/?data=' + resp.content)
    #     print r

    def test_authenticate(self):
        a = 'CN=051@xxx@0220503197505050871@1,OU=Individual-1,OU=Local RA,O=CFCA TEST CA,C=CN'

        # resp = requests.post(VERIFY_GATEWAY + '/Sign', data=a)
        r = self.get('/api/usb/?data=' + a)
        # r = self.get('/api/usb/?data=' + resp.content)

        reqID = Usb.objects.all().values('req_id')
        # print reqID[0]['req_id']


        data = {
            "name": "xxx",
            "id": "0220503197505050871",
            "req_id": reqID[0]['req_id']
        }

        post = self.post('/api/usbkey/', data=data, status_code=200)
