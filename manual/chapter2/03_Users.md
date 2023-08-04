用户部分
======

> 首次撰写：2017-01-14

> 最后修改：-

#### 用户中心接口


|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
| /api/me/profile/ | GET / PUT|登录用户|用户信息 目前缺少用户等级|
| /api/me/avatar/ | GET / PUT|登录用户|设置用户头像|
| /api/me/nick/ | GET / PUT|登录用户|设置用户昵称(马甲)|
| /api/me/address/ | GET / POST / PUT / DELETE|登录用户|用户地址列表|
| /api/me/contains/ | GET / POST|登录用户|用户手机通讯录提交对比接口|
| /api/me/conact/ | GET / PUT / DELETE|登录用户|我的好友|
| /api/me/noteices/ | GET | 登录用户 | 消息中心 |
| /api/me/blacklist/ | GET / PUT / DELETE|登录用户|黑名单|
| /api/me/bankcard/ | GET / PUT / DELETE|登录用户|银行卡|

#### 用户搜索接口

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
|/api/users/|GET|登录用户|用户搜索(列表)|
|/api/users/{pk}|GET|登录用户|用户详情|
|/api/users/{pk}/report/|GET|登录用户|为举报接口|
|/api/users/{pk}/invite/|GET|登录用户|邀请加好友|
|/api/users/{pk}/confirm/|GET|登录用户|邀请好友确认|
