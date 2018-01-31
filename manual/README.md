大众版开发文档
=====

|日期	|版本|	作者/修改者|	描述	|审核人|
| :-- | :-- | :-- | :-- | :-- |
| 2017-01-13 | V1.0 | bopo.wang| - | - |

#### 测试工具

- curl [使用方法](http://ju.outofmemory.cn/entry/84875)
- http [安装方法](http://yhz.me/blog/use-httpie.html)
- 另外还有个图形化测试工具 [RestClient](http://www.oschina.net/p/restclient)
- 或者使用`firefox` 的 `RestClient` 插件。
- 谷歌浏览器可以使用 `postman`

#### 测试方法

这里主要以http为主，各位高手可以举一反三，呵呵。

```
http [method] [url]
```

> 注意：关于api的GET参数说明，api后面跟随的`{pk}`或者`{id}` 是一个意思，代表改资源(`resource`)的主键.

