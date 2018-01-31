#参考资料

- [RESTful API 设计指南](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)

二维码扫描格式定义(初稿)
====================

二维码内容为一个 json 格式的数据.
数据格式为
```json
{
	type:<type>,
	data:<data> // `data` 内容为 `json` 内容转 `hex`
}
```

data 内容根据不同接口而变化，具体定义见下表

注: 
 - 所有 `<var>` 标签数据为可变数据
 - 类似 `<('receipt', '收据'), ('borrow', '借条'), ('owe', '欠条')>` 的数据为可变枚举
 

扫描加好友(邀请)
-------------
```json
type: invite
data: {
	url:<url>,
}

合约扫描(借条，欠条)
-----------------
```json
type: contract
data: {
	type:<('receipt', '收据'), ('borrow', '借条'), ('owe', '欠条')>
	status:<('', '无状态'), ('agree', '同意'), ('reject', '拒绝')>
	uri:<uri>,
	id:<id>,
}
```
交易(转账，收款)
-----------------
```json
type: contract
data: {
	type:<('transfer', '转账'),('receiver', '收款'),('thirty', '第三方')>
	status:<('normal', '无状态'), ('agree', '同意'), ('reject', '拒绝')>
	uri:<uri>,
	id:<id>,
}
```
支付操作(待定)
-----------------
```json
type: payment
data: {
	....
}
```
PC 端扫描登录
-----------------
```json
type: qrlogin
data: {
	scan:/api/qrlogin/<key>/scan/,
	done:/api/qrlogin/<key>/done,
	cancel:/api/qrlogin/<key>/cancel/,
}
```