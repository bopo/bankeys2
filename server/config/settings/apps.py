# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from .base import *
except ImportError as e:
    raise e

INSTALLED_APPS += (
    'service.frontend',
    'service.trade',
    'service.kernel',
    'service.message',
    'service.consumer',
    'service.restauth',
    'service.signature',
    'service.restauth.registration',
    'service.dashboard',
    'service.passport',

    'filters',
    'imagekit',
    'reversion',
    'easy_select2',
    'import_export',
    'daterange_filter',
    'constance',
)

RONGCLOUD_APPKEY = env('RONGCLOUD_APPKEY', default='ik1qhw09ifflp')
RONGCLOUD_SECRET = env('RONGCLOUD_SECRET', default='kfx3v7mffJeaJt')

JPUSH_APPKEY = env('JPUSH_APPKEY', default='496daf24808978b12e4e0505')
JPUSH_SECRET = env('JPUSH_SECRET', default='6e449bd8dd4dd2e5dff00c02')
JPUSH_OPTIONS = {"time_to_live": 86400, "sendno": 12345, "apns_production": False}

IDDENTITY_APPKEY = env('IDDENTITY_APPKEY', default='69tx91g3kpzlqkndszzofj38fr')
IDDENTITY_GATEWAY = env('IDDENTITY_GATEWAY', default='https://10.7.7.71:3002/api/register')

# VERIFY_GATEWAY = env('VERIFY_GATEWAY', default='http://127.0.0.1:8080')
VERIFY_GATEWAY = env('VERIFY_GATEWAY', default='http://10.7.7.22:9090')
# 查询银行卡详情
BANK_CARD = env('BANK_CARD', default='http://127.0.0.1:5000/bank')
# 第三方接口
PASSPORT = env('PASSPORT', default='http://10.7.7.85:3000')

CONSTANCE_REDIS_CONNECTION = env('CELERY_BROKER_URL', default='redis://localhost:6379/0')

# 银行卡接口
PAYMENT_INTEFACE = env('PAYMENT_INTEFACE', default='http://10.7.7.85:8000')

NOTICE_TYPE_MSGS = {
    'identity': '认证完成',
    'contract': '合约完成',
    'payment': '支付成功',
    'receive': '收货成功',
    'refunds': '退货成功'
}

BANKID = (
    # ('542', u'重庆三峡银行'),
    # ('100', u'邮政储蓄银行'),
    # ('102', u'中国工商银行'),
    # ('103', u'中国农业银行'),
    # ('104', u'中国银行'),
    # ('105', u'建设银行'),
    # ('301', u'交通银行'),
    # ('302', u'中信银行'),
    # ('303', u'中国光大银行'),
    # ('304', u'华夏银行'),
    # ('305', u'中国民生银行'),
    # ('306', u'广东发展银行'),
    # ('307', u'平安银行'),
    # ('308', u'招商银行'),
    # ('309', u'兴业银行'),
    # ('310', u'上海浦东发展银行'),
    # ('311', u'恒丰银行'),
    # ('316', u'浙商银行'),
    # ('317', u'渤海银行'),
    # ('422', u'河北银行'),
    # ('401', u'上海银行'),
    # ('403', u'北京银行'),
    # ('424', u'南京银行'),
    # ('423', u'杭州银行'),
    # ('434', u'天津银行'),
    # ('408', u'宁波银行'),
    # ('409', u'齐鲁银行'),
    # ('440', u'徽商银行'),
    # ('442', u'哈尔滨银行'),
    # ('443', u'贵阳银行'),
    # ('447', u'兰州银行'),
    # ('448', u'南昌银行'),
    # ('450', u'青岛银行'),
    # ('888', u'中金网银无卡'),
    # ('889', u'中金网银'),
    # ('891', u'金科无卡'),
    # ('892', u'银联代扣'),
    # ('900', u'收单机构（900）'),
    # ('700', u'CFCA模拟银行'),
    # ('1405', u'广东农商行'),
    # ('1565', u'颖淮农商行'),
    # ('1513', u'重庆农村商业银行'),

    ('CCB', u'中国建设银行'),
    ('AEON', u'AEON信贷'),
    ('ABC', u'中国农业银行'),
    ('AHNX', u'安徽省农村信用社联合社'),
    ('ASCCB', u'安顺市商业银行'),
    ('BCCARD', u'BC卡公司'),
    ('BCEL', u'BCEL'),
    ('BCM', u'交通银行'),
    ('BEA', u'东亚银行'),
    ('BEEB', u'鄞州银行'),
    ('BHRCB', u'天津滨海农村商业银行'),
    ('BJCCB', u'宝鸡市商业银行'),
    ('BJRCB', u'北京农村商业银行'),
    ('BNUBANK', u'大西洋银行'),
    ('BOAS', u'鞍山银行'),
    ('BOAY', u'安阳银行'),
    ('BOB', u'北京银行'),
    ('BOBBW', u'广西北部湾银行'),
    ('BOBD', u'保定银行'),
    ('BOC', u'中国银行'),
    ('BOCD', u'成都银行'),
    ('BOCS', u'长沙银行'),
    ('BOCY', u'朝阳银行'),
    ('BOCZ', u'沧州银行'),
    ('BODD', u'丹东银行'),
    ('BODL', u'大连银行'),
    ('BODY', u'德阳银行'),
    ('BOFS', u'抚顺银行'),
    ('BOFX', u'阜新银行'),
    ('BOGL', u'桂林银行'),
    ('BOGS', u'甘肃银行'),
    ('BOGY', u'贵阳银行'),
    ('BOGZ', u'赣州银行'),
    ('BOHB', u'鹤壁银行'),
    ('BOHH', u'新疆汇和银行'),
    ('BOHLD', u'葫芦岛银行'),
    ('BOHRB', u'哈尔滨银行'),
    ('BOHS', u'衡水银行'),
    ('BOHX', u'福建海峡银行'),
    ('BOHZ', u'湖州银行'),
    ('BOIMC', u'内蒙古银行'),
    ('BOJL', u'吉林银行'),
    ('BOJN', u'济宁银行'),
    ('BOJS', u'晋商银行'),
    ('BOJX', u'嘉兴银行'),
    ('BOKL', u'昆仑银行'),
    ('BOLF', u'廊坊银行'),
    ('BOLH', u'漯河银行'),
    ('BOLJ', u'龙江银行'),
    ('BOLY', u'洛阳银行'),
    ('BOLZ', u'柳州银行'),
    ('BONC', u'南昌银行'),
    ('BONX', u'宁夏银行'),
    ('BOPDS', u'平顶山银行'),
    ('BOPY', u'濮阳银行'),
    ('BOQH', u'青海银行'),
    ('BOQHD', u'秦皇岛银行'),
    ('BOQZ', u'泉州银行'),
    ('BOS', u'上海银行'),
    ('BOSI', u'中银信用卡(国际)有限公司'),
    ('BOSJ', u'盛京银行'),
    ('BOSJS', u'石嘴山银行'),
    ('BOSMX', u'三门峡银行'),
    ('BOSQ', u'商丘银行'),
    ('BOSR', u'上饶银行'),
    ('BOSX', u'绍兴银行'),
    ('BOSZ', u'苏州银行'),
    ('BOTL', u'铁岭银行'),
    ('BOTZ', u'台州银行'),
    ('BOWH', u'乌海银行'),
    ('BOXC', u'许昌银行'),
    ('BOXIA', u'西安银行'),
    ('BOXJ', u'华融湘江银行'),
    ('BOXM', u'厦门银行'),
    ('BOXX', u'新乡银行'),
    ('BOXY', u'信阳银行'),
    ('BOYK', u'营口银行'),
    ('BOZJ', u'郑州银行'),
    ('BOZK', u'周口银行'),
    ('BOZMD', u'驻马店银行'),
    ('BOZZ', u'枣庄银行'),
    ('BSB', u'包商银行'),
    ('BXCCB', u'本溪市商业银行'),
    ('CBD', u'迪拜商业银行'),
    ('CBHB', u'渤海银行'),
    ('CDB', u'承德银行'),
    ('CDRCB', u'成都农村商业银行'),
    ('CEB', u'中国光大银行'),
    ('CGB', u'广发银行'),
    ('CGSXCB', u'重庆三峡银行'),
    ('CHAB', u'长安银行'),
    ('CHBANK', u'创兴银行'),
    ('CIB', u'兴业银行'),
    ('CITIB', u'花旗银行'),
    ('CITIC', u'中信银行'),
    ('CITICKW', u'中信嘉华银行有限公司'),
    ('CJCCB', u'江苏长江商业银行'),
    ('CMB', u'招商银行'),
    ('CMBC', u'中国民生银行'),
    ('CQCB', u'重庆银行'),
    ('CQRCB', u'重庆农村商业银行'),
    ('CSC', u'CSC'),
    ('CSRCB', u'常熟农村商业银行'),
    ('CYBANK', u'集友银行'),
    ('CZB', u'浙商银行'),
    ('CZCB', u'浙江稠州银行'),
    ('CZCCB', u'长治银行'),
    ('DBS', u'星展银行'),
    ('DFS', u'发现金融服务公司'),
    ('DGCB', u'东莞银行'),
    ('DRCB', u'东莞农村商业银行'),
    ('DSBANK', u'大新银行'),
    ('DTCCB', u'大同市商业银行'),
    ('DYCCB', u'东营银行'),
    ('DZB', u'德州银行'),
    ('DZCCB', u'达州市商业银行'),
    ('EGB', u'恒丰银行'),
    ('FDB', u'富滇银行'),
    ('FJNX', u'福建省农村信用社联合社'),
    ('FSSSNX', u'佛山市三水区农村信用合作社'),
    ('GDHXCB', u'广东华兴银行'),
    ('GDNX', u'广东省农村信用社联合社'),
    ('GDNYB', u'广东南粤银行'),
    ('GRCB', u'广州农村商业银行'),
    ('GSNX', u'甘肃省农村信用社联合社'),
    ('GXNX', u'广西农村信用社联合社'),
    ('GZCB', u'广州银行'),
    ('GZNX', u'贵州省农村信用社联合社'),
    ('HANABANK', u'韩亚银行'),
    ('HBB', u'河北银行'),
    ('HBCL', u'湖北银行'),
    ('HBNX', u'河北省农村信用社联合社'),
    ('HDCB', u'邯郸银行'),
    ('HKB', u'汉口银行'),
    ('HKURCB', u'海口联合农商银行'),
    ('HLJNX', u'黑龙江省农村信用社联合社'),
    ('HMCCB', u'哈密市商业银行'),
    ('HNNX', u'河南省农村信用社联合社'),
    ('HNRCC', u'海南省农村信用社联合社'),
    ('HSB', u'徽商银行'),
    ('HSBANK', u'恒生银行'),
    ('HSBC', u'汇丰银行'),
    ('HUBNX', u'湖北省农村信用社联合社'),
    ('HUNNX', u'湖南省农村信用社联合社'),
    ('HXB', u'华夏银行'),
    ('HZB', u'杭州银行'),
    ('IBK', u'企业银行'),
    ('ICBC', u'中国工商银行'),
    ('JCCB', u'晋城银行'),
    ('JDZCCB', u'景德镇商业银行'),
    ('JHCCB', u'金华银行'),
    ('JJCCB', u'九江银行'),
    ('JLNX', u'吉林省农村信用社联合社'),
    ('JNRCB', u'江南农村商业银行'),
    ('JSB', u'江苏银行'),
    ('JSNX', u'江苏省农村信用社联合社'),
    ('JXNX', u'江西省农村信用社联合社'),
    ('JYRCB', u'江阴农村商业银行'),
    ('JZB', u'锦州银行'),
    ('JZCB', u'晋中银行'),
    ('JZCCB', u'焦作市商业银行'),
    ('KORLA', u'库尔勒市商业银行'),
    ('KSRCB', u'昆山农村商业银行'),
    ('LNNX', u'辽宁省农村信用社联合社'),
    ('LOTTE', u'韩国乐天'),
    ('LPSCCB', u'六盘水市商业银行'),
    ('LSB', u'临商银行'),
    ('LSCCB', u'乐山市商业银行'),
    ('LSZCCB', u'凉山州商业银行'),
    ('LWB', u'莱商银行'),
    ('LYCB', u'辽阳银行'),
    ('LZCB', u'兰州银行'),
    ('LZCCB', u'泸州市商业银行'),
    ('MYCCB', u'绵阳市商业银行'),
    ('NBCB', u'宁波银行'),
    ('NBDH', u'宁波东海银行'),
    ('NBTS', u'宁波通商银行'),
    ('NCB', u'南洋商业银行'),
    ('NCCCB', u'南充市商业银行'),
    ('NHRCB', u'广东南海农村商业银行'),
    ('NJCB', u'南京银行'),
    ('NMGNX', u'内蒙古农村信用社联合社'),
    ('OCBC', u'华侨银行'),
    ('ORDOS', u'鄂尔多斯银行'),
    ('PAB', u'平安银行'),
    ('PJCCB', u'盘锦市商业银行'),
    ('PSBC', u'中国邮政储蓄银行'),
    ('PZHCCB', u'攀枝花市商业银行'),
    ('QDCCB', u'青岛银行'),
    ('QDRCB', u'青岛市农村商业银行'),
    ('QHNX', u'青海省农村信用社联合社'),
    ('QJCCB', u'曲靖市商业银行'),
    ('QLB', u'齐鲁银行'),
    ('QSB', u'齐商银行'),
    ('RZB', u'日照银行'),
    ('SANGSUMG', u'韩国三星卡公司'),
    ('SCBL', u'渣打银行'),
    ('SCNX', u'四川省农村信用社联合社'),
    ('SDEB', u'顺德农村商业银行'),
    ('SDNX', u'山东省农村信用社联合社'),
    ('SHBANK', u'新韩银行'),
    ('SHBB', u'上海商业银行'),
    ('SHCARD', u'新韩卡公司'),
    ('SHXNX', u'陕西省农村信用社联合社'),
    ('SKKB', u'韩国国民银行'),
    ('SMBC', u'日本三井住友卡公司'),
    ('SNCCB', u'遂宁市商业银行'),
    ('SPDB', u'上海浦东发展银行'),
    ('SRCB', u'上海农村商业银行'),
    ('SXNX', u'山西省农村信用社联合社'),
    ('SZRCB', u'深圳农村商业银行'),
    ('TAB', u'泰安市商业银行'),
    ('TCRCB', u'太仓农村商业银行'),
    ('TFBANK', u'大丰银行'),
    ('TIBET', u'西藏银行'),
    ('TJCB', u'天津银行'),
    ('TJRCB', u'天津农村商业银行'),
    ('TSCCB', u'唐山市商业银行'),
    ('UCCB', u'乌鲁木齐市商业银行'),
    ('UNKNOW', u'Al Baraka Bank(Pakistan)'),
    ('UOBANK', u'大华银行'),
    ('WFCCB', u'潍坊银行'),
    ('WHBANK', u'永亨银行'),
    ('WHCCB', u'威海市商业银行'),
    ('WHNX', u'武汉市农村信用社联合社'),
    ('WHRCB', u'武汉农村商业银行'),
    ('WJRCB', u'吴江农村商业银行'),
    ('WLBANK', u'永隆银行'),
    ('WOORI', u'友利银行'),
    ('WXRCB', u'无锡农村商业银行'),
    ('WZCB', u'温州银行'),
    ('XJNX', u'新疆农村信用社联合社'),
    ('XTB', u'邢台银行'),
    ('YANCCB', u'雅安市商业银行'),
    ('YBCCB', u'宜宾市商业银行'),
    ('YDRCB', u'山西尧都农村商业银行'),
    ('YKYH', u'营口沿海银行'),
    ('YNKMNX', u'昆明市农村信用社联合社'),
    ('YNNX', u'云南省农村信用社联合社'),
    ('YQCCB', u'阳泉市商业银行'),
    ('YRRCB', u'黄河农村商业银行'),
    ('YTCB', u'烟台银行'),
    ('YXCCB', u'玉溪市商业银行'),
    ('ZGCCB', u'自贡市商业银行'),
    ('ZHHRCB', u'珠海华润银行'),
    ('ZHRCB', u'珠海农村商业银行'),
    ('ZJGRCB', u'张家港农村商业银行'),
    ('ZJKCCB', u'张家口市商业银行'),
    ('ZJMTB', u'浙江民泰商业银行'),
    ('ZJNX', u'浙江省农村信用社联合社'),
    ('ZJTLCB', u'浙江泰隆商业银行'),
    ('ZYCCB', u'遵义市商业银行'),
    ('DYLSCZ', u'东营莱商村镇银行'),
    ('HZUB', u'杭州联合农村商业银行'),
)

SCAN_TIMEOUT = 60

CONSTANCE_CONFIG = {
    'BORROW': ('', '借款模板'),
    'RECEIPT': ('', '收据模板'),
    'OWE': ('', '欠条模板'),
    'SIGNIN': ('', '登陆模板'),
    'SIGNUP': ('', '注册模板'),
}

CONSUMPTION_TYPE = (
    ('transfer', '转账'),
    ('receiver', '收款'),
    ('thirty', '第三方'),
)

CONTRACT_TYPE = (
    ('signin', '第三方登陆'),
    ('signup', '第三方注册'),
    ('payment', '第三方支付'),
    ('receive', '第三方收货'),
    ('refunds', '第三方退货'),
    ('transfer', '转账'),
    ('receiver', '收款'),
    ('receipt', '收据'),
    ('borrow', '借条'),
    ('owe', '欠款条'),
)
