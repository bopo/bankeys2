以下内容待定
----------
|字段|描述|
|-|-|
|display|插件展示内容|
|content|待签名数据源|
|hash1|Md5(dispaly) 用于校验显示内容|
|hash2|Md5(content+hash1) 用于校验证待签名和显示内容|
|displayUrl|插件获取展示内容的请求地址|
|contentUrl|插件获取待签内容的请求地址|
|type| type=0时，通过content和display字段获取显示和待签内容 <br>type=1时，通过content和displalyUrl字段获取显示和待签内容<br>type=2时，通过contentUrl和displayUrl获取显示和待签内容"|
|action|动作类型|
|pkg|手机客户端应用包名|

```json
{
	'display': 'signin',
	'content': '',
	'hash1': '',
	'hash2': '',
	'displayUrl': '',
	'contentUrl': '',
	'type': '',
	'action': '',
	'pkg': '',
}
```



### 验签服务流程

```sequence
participant 移动端
participant 服务器
participant 验签服务
移动端->服务器: 发送签名密文
服务器-->验签服务: 转发密文
验签服务-->服务器: 返回验签解密数据
Note over 服务器: 获得明文并处理业务
服务器-->验签服务: 发送返回数据
验签服务-->>服务器: 返回签名密文
服务器->移动端: 返回签名密文
```
