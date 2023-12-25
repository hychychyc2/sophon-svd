## 介绍
此例程可以模拟sophon-net/litos前端post请求来调试stream-server demo，并且提供了简单测试性能和计算cpu,tpu占用的脚本

## 常用命令
前端
python3 task_list.py #模拟查询任务列表请求
python3 create.py task_id #模拟创建任务请求
python3 query.py task_id# 模拟查询任务状态请求
python3 delete.py task_id# 模拟删除任务请求
bash start.sh start_ids end_ids #批量创建任务，支持数字id
测试
bash caculate.sh #计算cpu和tpu占用率
bash test_load.sh #测试cpu和tpu占用率
bash test_channel.sh #查询使得stream业务不阻塞最高的路数
bash check_pipefull.sh #查询stream业务log文件内是否包含阻塞
python3 post.py #模拟stream结果上报

