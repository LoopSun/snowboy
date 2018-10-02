# snowboy
snowflake分布式worker的workerID解决方案

- Restful API交互
- Base Auth认证
- 随机算法生成ID

1. 请求WorkerID
```
GET /snowflake/customer-id
```
#######返回
```
{
    "id": 123
}
```
2. 心跳WorkerID(dead time = 300s)
```
PUT /snowflake/customer-id
{
    "id": 123
}
```
#######返回
```
{
    "id": 123
}
```
3. 删除WorkerID
```
DELETE /snowflake/customer-id
{
    "id": 123
}
```
#######返回
```
{
    "id": 123
}
```