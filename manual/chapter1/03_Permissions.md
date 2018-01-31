权限认证说明
=====


#### 用户等级

- `任意用户` 没有注册的用户
- `登录用户` 或者叫 `认证用户` 注册并登录的用户
- `高级用户` 系统级用户，高级管理员，用于api底层统计等使用

#### 认证方式
- 用户登录后会返回一个josn,其中`key`值则为认证的码。
- 访问需要认证用户的`API`时，在请求的 `http headers` 里加上该码便可。
- 格式例如： `Authorization:Token 11eb2b41ead9af78cd4c0b9375cb893ed2004d1e`
- 注意：Token 后面有空格。

#### 举例说明：

```
http GET http://10.7.7.22/api/me/profile/ Authorization:Token\ 11eb2b41ead9af78cd4c0b9375cb893ed2004d1e
```

如果提示如下信息，说明登录过期，重新登录。

http 状态码为 40x

```json
{
    "detail": "Invalid token"
}
```


