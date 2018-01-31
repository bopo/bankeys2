# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import jsonfield
import short_url
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.contenttypes import fields as generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField
from model_utils import Choices
from model_utils.models import TimeStampedModel, StatusModel
from pilkit.processors import ResizeToFill
from rest_framework.serializers import ValidationError
from voluptuous import extra

from config.settings.apps import BANKID
from service.kernel.tasks import send_verify_push
from service.kernel.utils.jpush_audience import jpush_alias, jpush_extras, Pusher


class AbstractActionType(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, blank=True, default=None)
    content_object = generic.GenericForeignKey('content_type', 'object_id', )

    def validate_unique(self):
        if (self.__class__.objects.filter(owner=self.owner, object_id=self.object_id,
                                          content_type=self.content_type).exists()):
            raise ValidationError({'detail': 'The record already exists. '})

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        # email = self.normalize_email(email)
        user = self.model(username=username,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, True, **extra_fields)


class CustomUser(AbstractUser):
    """
    Concrete class of AbstractEmailUser.
    Use this if you don't need to extend EmailUser.
    """
    REQUIRED_FIELDS = []
    GENDER_CHOICES = (('male', '男'), ('female', '女'))
    mobile = models.CharField(_(u'手机号码'), max_length=25, db_index=True, blank=True)
    verify = models.CharField(_(u'短信码'), max_length=5, blank=True)
    device = models.CharField(_(u'设备号'), max_length=100, blank=False, null=False)
    level = models.CharField(_(u'用户等级'), max_length=100, blank=False, null=False)
    credit = models.IntegerField(_(u'用户积分'), default='50')
    objects = CustomUserManager()

    def short(self):
        short_url.encode_url(self.pk)


class Profile(models.Model):
    '''
    该接口更新接受PUT方法
    性别字段英文对应汉字为:
    male:男
    female:女
    提交的数据要用英文.获取时候api也是英文, 要客户端自己做下转换.
    '''
    GENDER_CHOICES = (('', '未知'), ('male', '男'), ('female', '女'))
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, db_index=True, related_name='profile')
    name = models.CharField(verbose_name=_(u'姓名'), blank=True, max_length=100, db_index=True)
    nick = models.CharField(verbose_name=_(u'昵称'), blank=True, null=True, max_length=100, db_index=True, default='')
    phone = models.CharField(verbose_name=_(u'银行预留电话'), default='', blank=True, max_length=64)
    gender = models.CharField(verbose_name=_(u'性别'), max_length=10, choices=GENDER_CHOICES, default=u'male')
    idcard = models.CharField(verbose_name=_(u'身份证'), max_length=100, default='')
    bankcard = models.CharField(verbose_name=_(u'银行卡号'), max_length=100, default='')
    birthday = models.DateField(_(u'生日'), blank=True, null=True)
    avatar = ProcessedImageField(verbose_name=_(u'头像'), upload_to='avatar', processors=[ResizeToFill(320, 320)],
                                 format='JPEG', null=True, default='avatar/default.jpg')
    friend_verify = models.BooleanField(verbose_name=_(u'加好友时是否验证'), default=False)
    mobile_verify = models.BooleanField(verbose_name=_(u'是否允许手机号查找'), default=False)
    name_public = models.BooleanField(verbose_name=_(u'是否公开姓名'), default=False)

    @property
    def qr(self):
        return ''

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'用户信息')
        verbose_name_plural = _(u'用户信息')


class Address(TimeStampedModel):
    '''
    用户地址信息
    '''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True)
    name = models.CharField(verbose_name=_(u'联系人'), blank=True, null=True, max_length=100, db_index=True)
    mobile = models.CharField(verbose_name=_(u'手机号'), blank=True, null=True, max_length=100, db_index=True)
    area = models.CharField(verbose_name=_(u'市区'), blank=True, null=True, max_length=255, db_index=True)
    city = models.CharField(verbose_name=_(u'城市'), blank=True, max_length=255, db_index=True)
    address = models.CharField(verbose_name=_(u'详细地址'), blank=True, null=True, max_length=255, db_index=True)
    default = models.BooleanField(verbose_name=_('默认地址'), default=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'用户地址')
        verbose_name_plural = _(u'用户地址')


class Contains(TimeStampedModel):
    '''
    用户通讯录
    '''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    contains = models.TextField(_(u'手机通讯录数据'), default='')

    def __unicode__(self):
        return self.owner

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'手机通讯录')
        verbose_name_plural = _(u'手机通讯录')


class Contact(TimeStampedModel, StatusModel):
    '''
    用户通讯录
    '''
    STATUS = Choices(('invite', '邀请'), ('confirm', '确认'), ('new', '新用户'))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('好友'), default='', related_name='friends')
    black = models.BooleanField(_('是否黑名单'), default=False)
    alias = models.CharField(_(u'备注别名'), max_length=100, default='')
    hide = models.BooleanField(_('别人不可见真名'), default=False)

    def __unicode__(self):
        return self.owner.username + '-' + self.friend.username

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'用户通讯录')
        verbose_name_plural = _(u'用户通讯录')
        unique_together = (("owner", "friend"),)


class Bankcard(TimeStampedModel):
    '''
    银行卡信息
    '''
    TYPE_CHOICES = (('借记卡', '借记卡'), ('贷记卡', '贷记卡'),)
    FLAG_CHOICES = (('', ''), ('收', '收'),)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True)
    cover = ProcessedImageField(verbose_name=_(u'银行logo'), upload_to='bank', processors=[ResizeToFill(320, 320)],
                                format='JPEG', null=True, default='banks/default.jpg')
    bank = models.CharField(verbose_name=_(u'所属银行'), blank=True, max_length=50, default='', choices=BANKID, )
    card = models.CharField(verbose_name=_(u'银行卡号'), blank=True, max_length=50, default='', unique=True)
    suffix = models.CharField(verbose_name=_(u'卡号后缀'), max_length=10, default='')
    type = models.CharField(verbose_name=_('卡片类型'), max_length=10, choices=TYPE_CHOICES, default='')
    flag = models.CharField(verbose_name=_('卡片用途'), max_length=10, choices=FLAG_CHOICES, default='')

    def __unicode__(self):
        return '%s - %s' % (self.bank, self.card)

    def __str__(self):
        return self.__unicode__()

    def save(self, *args, **kwargs):
        # bcard = requests.get(url='%s/%s' % (settings.BANK_CARD, self.card))
        # bcard = bcard.json()
        # bcard = bcard.get('result')
        #
        # self.bank = bcard.get('bank')
        # self.type = bcard.get('type')
        self.suffix = self.card[-4:]
        super(Bankcard, self).save()

    class Meta:
        verbose_name = _(u'用户银行卡')
        verbose_name_plural = _(u'用户银行卡')


class Settings(models.Model):
    '''
    该接口更新接受PUT方法
    电话号码绑定状态:
    fales: 未绑定
    true: 已绑定
    默认: 未绑定
    身份认证状态:
    fales: 未认证
    true: 已认证
    默认: 未认证
    证件类型字段英文对应汉字为:
    identity:居民身份证
    driver:驾驶证
    officers:军官证
    passport:护照
    提交的数据要用英文.获取时候api也是英文, 要客户端自己做下转换.
    '''
    GENDER_CHOICES = (('identity', '居民身份证'), ('driver', '驾驶证'), ('officers', '军官证'), ('passport', '护照'))
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, db_index=True, related_name='settings')
    name = models.CharField(verbose_name=_(u'姓名'), blank=True, max_length=255, db_index=True)
    nick = models.CharField(verbose_name=_(u'马甲'), blank=True, null=True, max_length=255, db_index=True)
    phone = models.CharField(verbose_name=_(u'电话'), default='', blank=True, max_length=64)
    type_phone = models.BooleanField(verbose_name=_(u'电话号码绑定状态'), default=False)
    id_card = models.CharField(verbose_name=_(u'证件号码'), default='', blank=True, max_length=64)
    document_type = models.CharField(verbose_name=_(u'证件类型'), max_length=10, choices=GENDER_CHOICES, default='identity')
    id_identity = models.BooleanField(verbose_name=_(u'身份认证'), default=False)
    avatar = ProcessedImageField(verbose_name=_(u'头像'), upload_to='avatar', processors=[ResizeToFill(320, 320)],
                                 format='JPEG', null=True)
    friend_verify = models.BooleanField(verbose_name=_(u'加好友时是否验证'), default=False)
    mobile_verify = models.BooleanField(verbose_name=_(u'是否允许手机号查找'), default=False)
    public_name = models.BooleanField(verbose_name=_(u'是否公开姓名'), default=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'settings')
        verbose_name_plural = _(u'settings')


class Notice(TimeStampedModel):
    '''
    用户消息
    '''
    NOTICE_CHOICE = (('identity', '认证'), ('contract', '合约'), ('payment', '支付'), ('receive', '收货'), ('refunds', '退货'),)
    subject = models.CharField(verbose_name=_(u'消息主题'), max_length=255, default='')
    content = models.TextField(verbose_name=_(u'消息正文'), default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name=_(u'推送给用户'))
    extra = jsonfield.JSONField(verbose_name=u'附加内容', default={'data': "", 'type': ""})
    type = models.CharField(verbose_name=_(u'消息类型'), max_length=100, choices=NOTICE_CHOICE)

    def __unicode__(self):
        return '%s: %s' % (self.owner, self.subject)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        ordering = ('-pk',)
        verbose_name = _(u'消息中心')
        verbose_name_plural = _(u'消息中心')


@receiver(signals.post_save, sender=Notice)
def post_notice_push(instance, created, **kwargs):
    if created:
        return jpush_extras(message=str(instance.subject), alias=[instance.owner.mobile], extras=instance.extra)


@receiver(signals.post_save, sender=Contact)
def post_contact_push(instance, created, **kwargs):

    if instance.status == 'invite':
        return jpush_extras(message=str(instance.owner.profile.name + '请求添加您为好友'), alias=[instance.friend.mobile],
                            extras={'type': instance.status, 'data': {
                                'friend_id': instance.friend.pk,
                            }})
    if not created:
        if instance.status == 'confirm':
            return jpush_extras(message=str(instance.owner.profile.name + '接受了您的添加请求'), alias=[instance.friend.mobile],
                                extras={'type': instance.status, 'data': {
                                    'friend_id': instance.owner.pk,
                                }})
