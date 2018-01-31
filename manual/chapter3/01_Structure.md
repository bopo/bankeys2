语法结构
===

#### 列表返回结果结构

| 参数 | 说明 | 备注 |
| -- | -- | -- |
| count | 记录总数 | ~ |
| next | 下页链接 | 不足分页返回null |
| previous | 上页链接 | 不足分页返回null |
| results | 结果记录 | ~ |
| url | 详细项目的url | 如果有这个参数，可以通过这个参数直接跳转 |


#### 调用举例

```json
{
    "count": 346,
    "next": "http://10.7.7.22/api/search/?page=2",
    "previous": null,
    "results": [
        {
            "url": "http://moo.life:8088/api/v1.0/stars/173/",
            "name": "李敏贞",
            "zodiac": "水瓶座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2015/01-04/0-PnEWvl.jpg"
        },
        
        .....

        {
            "url": "http://moo.life:8088/api/v1.0/stars/250/",
            "name": "刘在石",
            "zodiac": "狮子座",
            "gender": "",
            "avatar": "http://moo.life:8088/media/http%3A//img.mingxing.com/upload/thumb/2014/12-31/0-YpY9Yo.jpg"
        }
    ]
}
```

