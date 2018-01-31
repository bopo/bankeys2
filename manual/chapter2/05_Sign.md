
签名认证接口
==========


> 首次撰写：2017-01-14

> 最后修改：-

### 接口列表

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
|/api/sign/history/|GET|登录用户|签名历史, 签名详情|
|/api/sign/identity/|POST|登录用户|身份认证, 详情|
|/api/sign/callback/|POST|任意用户|视频验证(证书回调使用)|
|/api/sign/bankcard/|POST|登录用户|银行卡 PIN 号验证，识别等|
|/api/sign/validate/<id>|GET|登录用户|视频验证: id 为 验签 sdk 提供的|
|/api/sign/signature/|POST|登录用户|验签接口|
|/api/sign/counter/|POST|登录用户|临柜面审接口，四要素后直接请求，默认授权码123456，验证码654321|
|/api/sign/certificate/|POST|登录用户|证书查询 / 证书补发|