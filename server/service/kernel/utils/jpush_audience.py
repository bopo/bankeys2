# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import jpush
import time
from jpush import JPush
from jpush import common
from django.conf import settings


class Pusher:
    options = None
    debug = True
    production = False

    def __init__(self, **kwargs):
        # self.appkey = kwargs.get('appkey', settings.JPUSH_APPKEY)
        self.production = not self.debug
        self.sendno = int(time.time())

    def __del__(self):
        pass

    def send(self, message, *args, **kwargs):
        _jpush = JPush(settings.JPUSH_APPKEY, settings.JPUSH_SECRET)
        _jpush.set_logging("DEBUG") and settings.DEBUG

        alias = kwargs.get('alias')
        extra = kwargs.get('extra')

        push = _jpush.create_push()
        push.options = settings.JPUSH_OPTIONS
        push.options['sendno'] = self.sendno
        push.platform = jpush.all_

        # if alias:
        #     pass
        #
        # if extra:
        #     pass

        ios_msg = jpush.ios(alert=str(message), sound="default", extras=extra)
        android_msg = jpush.android(alert=str(message), extras=extra)

        push.audience = jpush.audience({"alias": alias})
        push.notification = jpush.notification(alert="bankeys push.", ios=ios_msg, android=android_msg)

        try:
            return push.send()
        except common.Unauthorized:
            raise common.Unauthorized("Unauthorized")
        except common.APIConnectionException:
            raise common.APIConnectionException("conn")
        except common.JPushFailure as e:
            raise e
        except Exception as e:
            raise e

    def alias(self, message, alias):
        return self.send(message=message, alias=alias)

    def all(self):
        pass

    def extra(self, message, alias, extra):
        return self.send(message=message, alias=alias, extra=extra)


def jpush_alias(message, *args, **kwargs):
    '''
    别名推送
    * @param  推送消息
    * @param  推送别名

    '''
    _jpush = JPush(settings.JPUSH_APPKEY, settings.JPUSH_SECRET)
    _jpush.set_logging("DEBUG") and settings.DEBUG

    push = _jpush.create_push()
    push.options = {"time_to_live": 86400, "sendno": 12345, "apns_production": not settings.DEBUG}
    push.audience = jpush.audience({"alias": args})

    push.notification = jpush.notification(alert=message)
    push.platform = jpush.all_

    try:
        return push.send()
    except common.Unauthorized:
        raise common.Unauthorized("Unauthorized")
    except common.APIConnectionException:
        raise common.APIConnectionException("conn")
    except common.JPushFailure as e:
        raise e
    except Exception as e:
        raise e


def jpush_all(message):
    '''
    全体推送
    * @param  推送消息

    '''
    _jpush = JPush(settings.JPUSH_APPKEY, settings.JPUSH_SECRET)
    _jpush.set_logging("DEBUG") and settings.DEBUG

    push = _jpush.create_push()
    push.options = {"time_to_live": 86400, "sendno": 12345, "apns_production": not settings.DEBUG}
    push.audience = jpush.all_
    push.notification = jpush.notification(alert=message)
    push.platform = jpush.all_

    try:
        return push.send()
    except common.Unauthorized:
        raise common.Unauthorized("Unauthorized")
    except common.APIConnectionException:
        raise common.APIConnectionException("conn")
    except common.JPushFailure:
        print ("JPushFailure")
    except:
        print ("Exception")


def jpush_extras(message, alias, extras, *args, **kwargs):
    '''
    别名推送（附加值）
    * @param  推送消息
    * @param  推送别名
    * @param  附加值

    '''
    _jpush = JPush(settings.JPUSH_APPKEY, settings.JPUSH_SECRET)
    _jpush.set_logging("DEBUG") and settings.DEBUG

    push = _jpush.create_push()
    push.options = {"time_to_live": 86400, "sendno": int(time.time()), "apns_production": False}
    settings.JPUSH_OPTIONS = {"time_to_live": 86400, "sendno": 12345, "apns_production": False}

    push.platform = jpush.all_

    ios_msg = jpush.ios(alert=str(message), sound="default", extras=extras)
    android_msg = jpush.android(alert=str(message), extras=extras)

    push.audience = jpush.audience({"alias": alias})
    push.notification = jpush.notification(alert="bankeys push", ios=ios_msg, android=android_msg)

    try:
        return push.send()
    except common.Unauthorized:
        raise common.Unauthorized("Unauthorized")
    except common.APIConnectionException:
        raise common.APIConnectionException("conn")
    except common.JPushFailure as e:
        raise e
    except Exception as e:
        raise e
