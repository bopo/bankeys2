# -*- coding: utf-8 -*-
import json
from random import randint

import requests
from django.contrib.auth import get_user_model

from service.passport.models import WaterLog
from service.signature.models import Signature
from service.trade.models import Transfer, Purchased, Contract
from .test_base import BaseAPITestCase
from service.restauth.models import VerifyCode


class APITestPassportTesk(BaseAPITestCase):
    """
    Case #1:
    - user profile: defined
    - custom registration: backend defined
    """
    MOBILE = '18574111101'
    VERIFY = '123456'

    def setUp(self):
        self.init()

        self.owenr = get_user_model()(mobile=self.MOBILE)
        self.owenr.save()

        self.log = WaterLog.objects.create(appkey='appkey', owner=self.owenr)

        self._generate_uid_and_token(user=self.owenr)

    def test_signup_validation(self):
        # 注册
        data = {
            'type': 'signup',
            'data': {
                'req_id': randint(0, 100000000),
                'token': self.token.key,
                'appkey': 'appkey',
                'uri': '/api/passport/signup/',
                'orderid': randint(0, 100000000),
            }
        }

        data = json.dumps(data)
        data = requests.post('http://10.7.7.22:9090/Sign', data=data)
        data = data.content

        resp = self.post('/api/passport/signup/', data=data.decode('hex'),
                         content_type='application/octet-stream',
                         status_code=200)

        print 333333333333333333

        ce = Contract.objects.filter(id=1)
        for a in ce:
            print a.type

        print 333333333333333333

        b = Signature.objects.all()
        for b in b:
            print b.type
            print b.owner
            print b.extra
            print b.signs
            print b.serial
            print b.expired
        print 333333333333333333
        # 解析数据
        data = resp.content.decode('hex')
        resp = requests.post('http://10.7.7.22:9090/Verify', data=data)
        sign = resp.json()

        try:
            rest = json.loads(sign.get('source').decode('hex').decode('hex'))
        except Exception:
            rest = json.loads(sign.get('source').decode('hex'))

        # 断言是否成功
        self.assertEqual(rest['errors'], 0)
        print rest

    def test_signin_validation(self):
        # 登陆
        data = {
            'type': 'signin',
            'data': {
                'req_id': randint(0, 100000000),
                'token': self.token.key,
                'appkey': 'appkey',
                'uri': '/api/passport/signin/',
                'orderid': randint(0, 100000000),
            }
        }
        data = json.dumps(data)
        data = requests.post('http://10.7.7.22:9090/Sign', data=data)
        data = data.content

        resp = self.post('/api/passport/signin/', data=data.decode('hex'), content_type='application/octet-stream',
                         status_code=200)

        # 解析数据
        data = resp.content.decode('hex')
        resp = requests.post('http://10.7.7.22:9090/Verify', data=data)

        sign = resp.json()
        try:
            rest = json.loads(sign.get('source').decode('hex').decode('hex'))
        except Exception:
            rest = json.loads(sign.get('source').decode('hex'))
        # 断言是否成功
        self.assertEqual(rest['errors'], 0)
        print rest

    def test_payment_validation(self):
        # 支付
        data = {
            'type': 'payment',
            'data': {
                'req_id': randint(0, 100000000),
                'openid': self.log.openid,
                'appkey': 'appkey',
                'uri': '/api/passport/payment/',
                'receive': '名字',
                'address': u'北京朝阳区',
                'orderid': randint(0, 100000000),
                'goods': {
                    'title': 1.00,
                    'amount': 123.00,
                }
            }
        }

        data = json.dumps(data)
        data = requests.post('http://10.7.7.22:9090/Sign', data=data)
        data = data.content

        resp = self.post('/api/passport/payment/', data=data.decode('hex'), content_type='application/octet-stream',
                         status_code=200)

        ce = Purchased.objects.filter(id=1)
        for a in ce:
            print a.type
            print a.title
            print a.amount
            print a.owner_id
            print a.signa_id
            print 23333333333333

        resp1 = self.get('/api/trade/purchase/')

        print resp1

        # 解析数据
        data = resp.content.decode('hex')
        resp = requests.post('http://10.7.7.22:9090/Verify', data=data)

        sign = resp.json()
        try:
            rest = json.loads(sign.get('source').decode('hex').decode('hex'))
        except Exception:
            rest = json.loads(sign.get('source').decode('hex'))
        # 断言第三方返回值是否成功
        self.assertEqual(rest['errors'], 0)

    def test_receive_validation(self):

        # 收货
        data = {
            'type': 'receive',
            'data': {
                'req_id': randint(0, 100000000),
                'openid': self.log.openid,
                'appkey': 'appkey',
                'uri': '/api/passport/receive/',
                'orderid': '123456',
            }
        }
        data = json.dumps(data)
        data = requests.post('http://10.7.7.22:9090/Sign', data=data)
        data = data.content

        resp = self.post('/api/passport/receive/', data=data.decode('hex'), content_type='application/octet-stream',
                         status_code=200)

        # 解析数据
        data = resp.content.decode('hex')
        resp = requests.post('http://10.7.7.22:9090/Verify', data=data)

        sign = resp.json()
        try:
            rest = json.loads(sign.get('source').decode('hex').decode('hex'))
        except Exception:
            rest = json.loads(sign.get('source').decode('hex'))
        # 断言是否成功
        self.assertEqual(rest['errors'], 0)
        print rest

    def test_refunds_validation(self):
        # 退货
        data = {
            'type': 'refunds',
            'data': {
                'req_id': randint(0, 100000000),
                'openid': self.log.openid,
                'appkey': 'appkey',
                'uri': '/api/passport/refunds/',
                'orderid': '123456',
            }
        }
        data = json.dumps(data)
        data = requests.post('http://10.7.7.22:9090/Sign', data=data)
        data = data.content

        resp = self.post('/api/passport/refunds/', data=data.decode('hex'),
                         content_type='application/octet-stream',
                         status_code=200)

        # 解析数据
        data = resp.content.decode('hex')
        resp = requests.post('http://10.7.7.22:9090/Verify', data=data)

        sign = resp.json()
        try:
            rest = json.loads(sign.get('source').decode('hex').decode('hex'))
        except Exception:
            rest = json.loads(sign.get('source').decode('hex'))
        # 断言是否成功
        self.assertEqual(rest['errors'], 0)
        print rest

    def test_push_validation(self):
        data = {
            'type': 'receive',
            'data': {
                'req_id': '请求唯一的id, 发起方随机生成',
                'appkey': 'appkey',
                'uri': '/api/passport/receive/',
                'openid': self.log.openid,
                'orders': {
                    'goods': {
                        'title': '',
                        'amount': '',
                        'quantity': '',
                    },
                    'users': {
                        'name': '',
                        'mobile': '',
                        'address': '',
                    },
                    'orderid': '',
                    'created': '',
                    'fee': '',
                    'discount': '',
                    'paymend': '',
                }
            }
        }

        # data = json.dumps(data)
        # data = requests.post('http://127.0.0.1:8080/Sign', data=data)
        # data = data.content.decode('hex')

        # resp = self.post('/api/passport/push/', data=data, status_code=200)
        resp = self.post('/api/passport/push/', data=data, content_type='application/json', status_code=200)

        # data = resp.content.decode('hex')
        # data = requests.post('http://10.7.7.22:9090/Verify', data=data)

        # print resp.content

    def test_identity_validation(self):

        payload = {
            "mobile": self.MOBILE
        }

        resp = self.post('/api/auth/registration/verify_mobile/', data=payload, status_code=200)
        self.assertEqual(resp.json['detail'], u'验证码已经成功发送')

        code = VerifyCode.objects.get(mobile=payload['mobile'])

        payload["verify"] = code.code
        resp = self.post('/api/auth/registration/', data=payload, status_code=201)
        self.assertTrue(bool(resp.json.get('key')))
        self.token = resp.json.get('key')

        payload = {
            "certId": "130435197406221691",
            "name": "刘鹏",
            "phone": "13141039522",
            "cardNo": "6227000014150347510",
            "bankID": "CCB",
            "level": "A",
            "frontPhoto": open('assets/media/avatar/default.jpg', 'rb'),
            "backPhoto": open('assets/media/avatar/default.jpg', 'rb'),
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token)
        resp = self.client.post('/api/sign/identity/', data=payload, format='multipart')
        self.assertEquals(resp.status_code, 200, msg=resp)

        print resp.content
