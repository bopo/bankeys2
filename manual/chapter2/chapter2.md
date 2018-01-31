<!-- toc -->

## 接口列表

#### APP 版本管理(安卓)

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
|/api/version/|GET|任意用户|安卓版本更新接口|

#### 用户搜索接口

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
|/api/users/|GET|登录用户|用户搜索(列表)|
|/api/users/{pk}|GET|登录用户|用户详情|
|/api/users/{pk}/report/|GET|登录用户|为举报接口|
|/api/users/{pk}/invite/|GET|登录用户|邀请加好友|
|/api/users/{pk}/confirm/|GET|登录用户|邀请好友确认|

#### 用户中心接口

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
|/api/me/profile/|GET / PUT|登录用户|用户信息 目前缺少用户等级|
|/api/me/avatar/|GET / PUT|登录用户|设置用户头像|
|/api/me/nick/|GET / PUT|登录用户|设置用户昵称(马甲)|
|/api/me/address/|GET / POST / PUT / DELETE|登录用户|用户地址列表|
|/api/me/notices/|GET|登录用户|用户通知消息|
|/api/me/conact/|GET / PUT / DELETE|登录用户|我的好友|
|/api/me/blacklist/|GET / PUT / DELETE|登录用户|黑名单|
|/api/me/bankcard/|GET / PUT / DELETE|登录用户|银行卡|

#### 用户认证接口

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
|/api/auth/registration/verify_mobile/|POST|任意用户|获取手机验证码|
|/api/auth/registration/|POST|任意用户|注册用户|

#### 聊天融云接口

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
|/api/im/group/|POST / GET|登录用户|POST 为创建组，会自动加创建人到组里|
|/api/im/group/<pk>join/|POST|登录用户|拉人进组|
|/api/im/group/<pk>quit/|GET|登录用户|退出组|
|/api/im/group/<pk>users/|GET|登录用户|组内成员列表|
|/api/im/group/<pk>dismiss/|GET|登录用户|解散组|
|/api/im/token/|GET|登录用户|获取融云的 token|

#### 交易合约接口

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
| /api/trade/purchase/ | GET | 登录用户 | 消费记录接口|
| /api/trade/purchase/{pk} | GET | 登录用户 | 消费记录接口 |
| /api/trade/contract/ | GET | 登录用户 | 合约记录接口 |
| /api/trade/contract/{pk} | GET | 登录用户 | 合约记录接口 |

#### 签名认证接口

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
| /api/sign/history/ | GET | 登录用户 |签名历史, 签名详情 |
| /api/sign/identity/ | POST | 登录用户 | 身份认证, 详情 |
| /api/sign/callback/| POST | 任意用户 | 视频验证(证书回调使用) |
| /api/sign/bankcard/| POST | 登录用户 | 银行卡 PIN 号验证，识别等 |
| /api/sign/validate/<id>| GET | 登录用户 | 视频验证: id 为 验签 sdk 提供的 |
| /api/sign/signature/| POST | 登录用户 | 验签接口 |
| /api/sign/counter/| POST | 登录用户 | 临柜面审接口，四要素后直接请求，默认授权码123456，验证码654321 |
| /api/sign/certificate/ | POST | 登录用户 | 证书查询 / 证书补发 |

