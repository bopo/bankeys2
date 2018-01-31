# 验签说明文档 初稿
如有任何异议请尽快提出

## 验签服务器（测试用）

```
http://10.7.7.22:9090
```

## 数据说明

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| endDate | 字符 | 证书到期时间 |
| subject | 字符 | 返回身份认证的 `DN` 参数 |
| respMsg | 字符 | 返回提示信息 |
| source | 字符 | 解密后的数据 (需要 hex 解码方可得到明文) 
| respCode | 字符 | 返回状态码 |
| issuer | 字符 | 发证机构 (暂时至于一个 CFCA)|
| startDate | 字符 | 证书开始时间 |
| serialNo | 字符 | 证书序列号或者叫证书号 |



## 操作方法
> 请求链接为: 验签服务器网址 + 下面方法
> 例如：http://10.7.7.22:9090/Verify 为验签操作的请求网址。
> 所有输入数据为 `post` 验签服务器 `body` 内

### 验签方法 (/Verify)
正常返回:

```json
{
    "endDate": "2018-12-05", 
    "subject": "CN=051@bankeys-personal@720161205@1, OU=Organizational-1, OU=Local RA, O=CFCA TEST CA, C=CN", 
    "respMsg": "成功", 
    "source": "376232323733366637353732363336353232336132323638363932323764", 
    "respCode": "0000", 
    "issuer": "CN=CFCA TEST SM2 OCA11, O=China Financial Certification Authority, C=CN", 
    "startDate": "2016-12-05", 
    "serialNo": "137815992676"
}
```

### 数据签名 (/Sign)
- 输入数据: 直接将需要的数据 POST 至服务端
- 返回数据: 是加密过的密文数据 


###1.查询证书状态 (/Query) 

> 状态定义: 3 = 未下载, 4 = 已下载, 5 = 冻结, 6 = 吊销
> 传入数据为用户证书中的 DN

正常返回

```json
{
    "respMsg": "成功", 
    "respCode": "0000", 
    "status": "3", 
    "serialNo": "2016814899",
    "startDate": "2016-12-12",
    "endDate": "2016-12-12",
}
```

异常返回

```json
{
    "respMsg": "errMsg", 
    "respCode": "3322"
}
```

###2.补发 (/Reissue) 
> 传入数据为用户证书中的 DN

正常返回
 
```json
{
    "authCode": "LS9HL3FLJ3", 
    "respMsg": "成功", 
    "respCode": "0000", 
    "serialNo": "2016824335"
}
```

异常返回

```json
{
    "respMsg": "证书不是激活状态", 
    "respCode": "3322"
}
```

###3.注销 (/Revoke) 
> 传入数据为用户证书中的 DN

正常返回

```json
{
    "respMsg":"成功",
    "respCode":"0000"
｝
```

异常返回
 
```json
{
    "respMsg": "证书不是激活状态", 
    "respCode": "3322"
}

```

