# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import re

from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models.usbkeys import Usb

import requests

# 验签地址
VERIFY_GATEWAY = 'http://10.7.7.22:9090'


@api_view(['GET', 'POST'])
def deposit(request):
    '''
       usb 验签接口
    '''
    if request.method == 'GET':

        print request.GET['data']

        try:
            obj, _ = Usb.objects.get_or_create(sin_data=request.GET['data'])
            # obj.save()
        except IOError:
            print "Error: 写入数据重复"
            return Response({'errors': 1, 'detail': '数据写入重复'})
    else:
        return Response({'errors': 1, 'detail': '请求类型错误'})

    return Response({'errors': 0, 'detail': '数据写入成功', 'req_id': obj.req_id})


@api_view(['POST'])
def usbkey(request):
    if request.method == 'POST':

        # 接收数据
        data = request.data
        name = data['name']
        idcard = data['id']
        req_id = data['req_id']
        # print req_id

        # 查询该条数据
        try:
            s_data = Usb.objects.get(req_id=req_id)
            # print st.sin_data
            sd = s_data.sin_data
            # sd = s_data.sin_data.decode('hex')
            print sd 
        except Exception as e:
            return e.message

        # 验签
        # resp = requests.post(VERIFY_GATEWAY + '/Verify', data=sd)
        # sign = resp.json()
        # print sign
        #
        # try:
        #     dd = sign.get('source').decode('hex').decode('hex')
        # except Exception as e:
        #     dd = sign.get('source').decode('hex')

        # 数据比较
        # print dd
        # CN=051@xxx@130427199405294118@1,OU=Individual-1,OU=Local RA,O=CFCA TEST CA,C=CN
        break_up = sd.split('@')
        break_name = break_up[1]
        break_idcard = break_up[2]

        if break_name == name:
            if break_idcard == idcard:
                return Response({'errors': 0, 'detail': 'ok'})
            return Response({'errors': 1, 'detail': '数据不一样'})
        else:
            return Response({'errors': 1, 'detail': '数据不一样'})

    else:
        return Response({'errors': 1, 'detail': '请求类型错误'})





# class UsbkeyViewSet(mixins.CreateModelMixin, GenericViewSet):
#     queryset = Usb.objects.all()
#     serializer_class = UsbSerializer
#
#     # @list_route(methods=['GET'])
#     # def push(self, request, *args, **kwargs):
#     #     serializer = self.get_serializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     self.perform_create(serializer)
#     #     return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         return self.perform_valid(serializer)
#
#     def perform_valid(self, serializer):
#         # serializer.save()
#         # serializer.data['id']
#         data = serializer.data
#         print data
#
#         # valid data
#         # 判断数据
#         # if data.get('id') == id:
#         #     pass
#         #
#         # elif data.get('name') == name:
#         #     pass
#
#         # 返回
#         return Response({'detail': 'ok'}, status=status.HTTP_200_OK)
#         return Response({'detail': 'error'}, status=status.HTTP_400_BAD_REQUEST)
