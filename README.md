# snowboy
snowflake分布式worker的workerID解决方案

- Restful API交互
- Base Auth认证
- 随机算法生成ID

1. 请求WorkerID
```
GET /snowflake/customer-id
```
- 返回
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
- 返回
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
- 返回
```
{
    "id": 123
}
```
4. Docker
- 运行代码根目录的buildDocker.sh打包镜像
```
sudo ./buildDocker.sh
```
- 或者直接使用发布好的镜像
```
cd docker && docker-compose up -d
```