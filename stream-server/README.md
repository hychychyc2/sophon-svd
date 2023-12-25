# stream-server

## 介绍
此框架意图是为了打通sophon-net与sophon-stream，通过json配置文件,使得底层算法与上层前端可以联动。
## 特性
本框架实现了简单的业务层逻辑demo和json配置文件转换功能。
本框架包含一个主要后端server，以flask框架搭建，由server进行接受前端json，并做任务下发和任务管理，每个任务对应一个stream算法进程和一个业务层逻辑进程，业务层也是由flask框架搭建。
## 准备sophon-stream算法
参考(../sophon-stream/README.md)根据算法需求准备好模型与数据，并完成stream编译，生成main函数接口，此接口为sophon-stream进程主要逻辑的入口，根据命名格式完成config命名，注意入口参数config一般以算法名称+'_demo'命名，算法名称为samples下文件目录名称。
算法定义了TYPE映射保存在server中，目前仅适配了license_plate_recognition
map_type={16:'license_plate_recognition'}

## server使用方式
由server进行接受前端json，并做任务下发和任务管理，包含线程池和端口管理。
提供了python接口
python3 server.py --stream_path="/path/to/stream"

其中包含服务如下,设置遵循sophon-net接口规则
/task/list 
完成查询任务列表功能
/task/create 
完成创建任务功能

/task/query  
完成查询任务状态功能

/task/delete
完成删除任务功能

## 创建任务功能
主要逻辑模块之一，包含以下模块

### build_config
```
def build_config(data):
    '''
    return :  demo_config_path,TaskID,Type
    '''
```
接受sophon-net请求并转换成stream config规则，此部分不同算法具有特异性，需要根据具体算法配置extend选项进行修改代码。
### build_task
```
def build_task(demo_config_path,task_id,Type,result_url):
    '''
    return :  0
    '''
```

起stream算法进程和业务层进程
stream算法进程 
完成算法,并将逐帧结果通过post请求推送到业务层

业务层进程 [client](#client使用方式)，业务层进程需要占用端口，默认从10001开始递增

## client使用方式
使用方式如下
默认参数
--task_id, type=str, default="0", help='id of task'
--type, type=int, default=0, help='type of algorithm'
--host, type=str, default="0.0.0.0", help='ip of host'
--port, type=int, default=11100, help='port of host'
--url, type=str, default="", help='report url'
由于算法是逐帧反馈的，所以具体业务需要对算法的结果进行反馈，逐帧反馈是不现实的，会严重占用带宽，需要业务层逻辑进行筛选。

实现了接受stream结果，并进行业务筛选(如车牌识别去重筛选告警功能)，此部分具有特异性，需要根据需求修改，并转换为sophon-net接口格式做出告警,并使用post请求做异步上报，亦可以保存json到本地文件。

本例程中只对连续出现n帧并且没有连续消失m帧的进行告警。可以根据需求在修改。


