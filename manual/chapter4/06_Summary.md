系统集成部分
====


> 首次撰写：2017-01-12

> 最后修改：2017-02-17


### 二维码/推送数据格式(注册、登录部分)

```json
{
	'type':'sginup', // action 详见 APP 接口表
	'data': {
		'req_id': '请求唯一的id, 发起方随机生成'
		'appkey': 'val', // 系统分配给商家的唯一标示
		'uri': '/api/passport/sginup/' // APP 服务器的 uri 路径
	}
}
```

### 推送数据格式

```json
{
	'type':'sginup', // action 详见 APP 接口表
	'data': {
		'req_id': '请求唯一的id, 发起方随机生成'
		'openid': '用户对应的唯一码',
		'appkey': 'val', // 系统分配给商家的唯一标示
		'uri': '/api/passport/sginup/' // APP 服务器的 uri 路径
	}
}
```

### 支付推送数据格式(包括二维码)

```json
{
	'type':'payment', // action 详见 APP 接口表
	'data': {
		'req_id': '请求唯一的id, 发起方随机生成'
		'openid': '用户对应的唯一码'
		'appkey': '系统分配给商家的唯一标示',
		'uri': '/api/passport/payment/'  // APP 服务器的 uri 路径
		'receive': '', 		// 收款方名字
		'orderid': '',		// 订单号码
		'goods':{
			'title': '',	// 商品名称 
			'amount': '',	// 支付价格
		}
	}
}
```

### 注册手机端返回内容(移动端到服务器)

```json
{
	'type':'payment', // action 详见 APP 接口表
	'data': {
		'req_id': '请求唯一的id, 发起方随机生成'
		'appkey': '系统分配给商家的唯一标示', 
		'token': '用户标示的token',
		'uri': '/api/passport/payment/',  // APP 服务器的 uri 路径
		'orderid': '',		// 订单号码
		'account': '',		// 银行账户
	}
}
```

### 手机端返回内容(移动端)

```json
{
	'type':'payment', // action 详见 APP 接口表
	'data': {
		'req_id': '请求唯一的id, 发起方随机生成'
		'openid': '用户对应的唯一码',
		'appkey': '系统分配给商家的唯一标示', 
		'uri': '/api/passport/payment/',  // APP 服务器的 uri 路径
		'orderid': '',		// 订单号码
		'account': '',		// 银行账户
	}
}
```


### 收货推送数据格式

```json
{
	'type':'receive', // action 详见 APP 接口表
	'data': {
		'req_id': '请求唯一的id, 发起方随机生成'
		'openid': '用户对应的唯一码'
		'appkey': 'val', // 系统分配给商家的唯一标示
		'uri': '/api/passport/receive/' // APP 服务器的 uri 路径
		'orders':{
			'goods': {
				'title': '', 	// 商品名称 
				'amount': '', 	// 支付价格
				'quantity': '', // 商品数量
			},
			'users': {
				'name': '',		// 用户姓名
				'mobile': '',	// 用户电话
				'address': '',	// 用户地址
			},
			'orderid': '',		// 订单号码
			'created': '',		// 下单时间
			'fee': '',			// 邮费
			'discount': '',		// 折扣
			'paymend': '',		// 实际支付
		}	
	}
}
```

### 收货手机端返回内容(移动端)
```json
{
	'type':'payment', // action 详见 APP 接口表
	'data': {
		'req_id': '请求唯一的id, 发起方随机生成',
		'openid': '用户对应的唯一码',
		'appkey': 'val', 				 // 系统分配给商家的唯一标示
		'uri': '/api/passport/payment/'  // APP 服务器的 uri 路径
		'orderid': '',		// 订单号码
	}
}
```

### 退货推送数据格式

```json
{
	'type':'refunds', // action 详见 APP 接口表
	'data': {
		'req_id': '请求唯一的id, 发起方随机生成',
		'openid': '用户对应的唯一码',
		'appkey': 'val', // 系统分配给商家的唯一标示
		'uri': '/api/passport/sginup/' // APP 服务器的 uri 路径
		'orders':{
			'goods': {
				'title': '', 	// 商品名称 
				'amount': '', 	// 支付价格
				'quantity': '', // 商品数量
			},
			'users': {
				'name': '',		// 用户姓名
				'mobile': '',	// 用户电话
				'address': '',	// 用户地址
			},
			'orderid': '',		// 订单号码
			'created': '',		// 下单时间
			'fee': '',			// 邮费
			'discount': '',		// 折扣
			'paymend': '',		// 实际支付
		}		
	}
}
```

### 退货手机端返回内容(移动端)

```json
{
	'type':'payment', // action 详见 APP 接口表
	'data': {
		'req_id': '请求唯一的id, 发起方随机生成',
		'openid': '用户对应的唯一码',
		'appkey': 'val', 				 // 系统分配给商家的唯一标示
		'uri': '/api/passport/payment/'  // APP 服务器的 uri 路径
		'orderid': '',		// 订单号码
	}
}
```