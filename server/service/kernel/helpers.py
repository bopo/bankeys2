# -*- coding: utf-8 -*-

import jpush as jpush
# import top
from django.conf import settings
from jinja2 import Template


def response(jsonobj, key):
    obj = jsonobj.get(key)
    suc = False

    if obj:
        success = obj.get('result').get('successful')

        if success is True:
            suc = True

        msg = obj.get('result').get('message')
    else:
        msg = obj.get('error_response').get('sub_msg')

    return [suc, msg]


def pushMessage(messages=None, extra=None, *args, **kwargs):
    template = Template(messages)
    messages = template.render(dict(*args, **kwargs))

    push = jpush.JPush(settings.JPUSH_APPKEY, settings.JPUSH_SECRET)
    push = push.create_push()

    push.notification = jpush.notification(alert=messages, ios=messages, android=messages)
    push.options = {"time_to_live": 86400, "sendno": 12345, "apns_production": False}
    push.platform = jpush.platform("ios", "android")
    push.send()


def do_push_msgs(msgs=None, mobile=None, registration_id=None, *args, **kwargs):
    opts = jpush.JPush(settings.JPUSH_APPKEY, settings.JPUSH_SECRET)
    push = opts.create_push()

    extras = {'mobile': mobile}

    push.notification = jpush.notification(alert=msgs)

    push.options = {"time_to_live": 86400, "apns_production": True, 'extras': extras}

    push.audience = jpush.audience(jpush.registration_id(registration_id)) if registration_id else jpush.all_
    push.platform = jpush.all_

    push.send()
