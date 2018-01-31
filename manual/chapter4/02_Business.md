商户服务部分
====


> 首次撰写：2017-01-12

> 最后修改：2017-01-13

### 商户数据字典

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| appkey | 字符 | 商户标示 |
| secret | 字符 | 商户密钥,用以计算签名 |
| name | 字符 | 商户名称 |
| account | 字符 | 商户收款账户 |
| callback | URL | 回调地址  |

### 功能列表:

* 生成登录二维码 [见二维码格式](06_Summary.md)
* 生成注册二维码 [见二维码格式](06_Summary.md) 
* 生成支付二维码 [见二维码格式](06_Summary.md)
* 支付、收货、退货的推送，推送需要回调URL。

### 接口列表:

| 节点 | 方法 | 功能 | 备注 |
|:---|:---:|:---:|:---:|
|/services/validate/{req_id}/ | POST | 第三方 APP 验证操作是否成功接口 | req_id 与生成时候的相同  |
|/services/callback/{action}/ | POST | 回调接口URI | action 与 APP 服务同 |
|/services/product/{pk} | GET / POST | 回调获取商品信息 | 待定 |
|/services/orders/ | GET / POST | 回调获取订单信息 | 待定 |

### 所有的返回格式:
| 字段 | 类型 | 说明 |
| --- | --- | --- |
| errors | 字符 | 错误状态 1=错误，0=正常 |
| detail | 字符 | 返回的状态消息 |

例如：
```json
{
	"errors": 1,
	"detail": "XXX 不正确"
}

```

### 应用后台
* 添加签约商户





