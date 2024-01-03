[简体中文](./README.md)
## sophon-net-stream介绍

## 简介
Sophon-net-stream Demo基于SophonSDK接口进行开发，目的是完成sophon-net与sophon-stream的联动，并将业务层逻辑加入其中，以达到实际业务应用的目的。包括基于sophon-stream算法模块，stream-server服务模块，stream-client测试模块。

SophonSDK是算能科技基于其自主研发的深度学习处理器所定制的深度学习SDK，涵盖了神经网络推理阶段所需的模型优化、高效运行时支持等能力，为深度学习应用开发和部署提供易用、高效的全栈式解决方案。目前可兼容BM1684/BM1684X/BM1688。

## 目录结构与说明

其中包含三个模块

sophon-stream算法模块，是sophon-sdk中多线程得高性能框架完成得算法模块，可以在sdk release 包中下载,详见stream[sophon-stream](./sophon-stream/README.md)

stream-server服务模块详见[stream-server](./stream-server/README.md)

stream-client测试模块详见[stream-client](./stream-client/README.md)
## 版本说明
| 版本    | 说明 | 
|--------|------------|
|0.1.0 |提供车牌识别算法接入,完成告警业务逻辑层demo，完成创建，删除，查询，上报任务服务，并提供cpu,tpu测试脚本。|
## 环境依赖
Sophon Demo主要依赖tpu-mlir、tpu-nntc、libsophon、sophon-ffmpeg、sophon-opencv、sophon-sail，其版本要求如下：
|sophon-demo|tpu-mlir |flask  |libsophon|sophon-ffmpeg|sophon-opencv|sophon-stream| 发布日期   |
|--------|------------| --------|---------|---------    |----------   | ------    | --------  |
| 0.1.9 | >=1.2.2     | >=3.1.7 | >=0.4.6 | >=0.6.0     | >=0.6.0     | >=3.7.0   | >=23.10.01|
| 0.1.8 | >=1.2.2     | >=3.1.7 | >=0.4.6 | >=0.6.0     | >=0.6.0     | >=3.6.0   | >=23.07.01|
| 0.1.7 | >=1.2.2     | >=3.1.7 | >=0.4.6 | >=0.6.0     | >=0.6.0     | >=3.6.0   | >=23.07.01|
| 0.1.6 | >=0.9.9     | >=3.1.7 | >=0.4.6 | >=0.6.0     | >=0.6.0     | >=3.4.0   | >=23.05.01|
| 0.1.5 | >=0.9.9     | >=3.1.7 | >=0.4.6 | >=0.6.0     | >=0.6.0     | >=3.4.0   | >=23.03.01|
| 0.1.4 | >=0.7.1     | >=3.1.5 | >=0.4.4 | >=0.5.1     | >=0.5.1     | >=3.3.0   | >=22.12.01|
| 0.1.3 | >=0.7.1     | >=3.1.5 | >=0.4.4 | >=0.5.1     | >=0.5.1     | >=3.3.0   |    -      |
| 0.1.2 | Not support | >=3.1.4 | >=0.4.3 | >=0.5.0     | >=0.5.0     | >=3.2.0   |    -      |
| 0.1.1 | Not support | >=3.1.3 | >=0.4.2 | >=0.4.0     | >=0.4.0     | >=3.1.0   |    -      |
| 0.1.0 | Not support | >=3.1.3 | >=0.3.0 | >=0.2.4     | >=0.2.4     | >=3.1.0   |    -      |
> **注意**：
> 1. 不同例程对版本的要求可能存在差异，具体以例程的README为准，可能需要安装其他第三方库。
> 2. BM1688与BM1684X/BM1684对应的sdk不是同一套，暂时还未发布到官网上。

## 如何部署
首先按照stream手册编译stream，根据算法需求及设备类型配置stream文件
根据[stream-server](./stream-server/README.md)开启服务

## 如何测试
根据[stream-client](./stream-client/README.md)测试

性能测试结果如下
| 设备类型 | cpu核 |	yolov5模型信息(batch,time,type,post)	| lprnet模型信息(batch,time,type,post) |	芯片 |	TPU利用率 |	cpu利用率 |	device 内存(M) | sys 内存(G) |	抽帧数 | 分析路数 |
|--------|------------| --------|---------|--------- |----------   | ------    | --------  |----------   | ------    | --------  |
|se5-16	|8	| 4b,0.021794,int8,cpu	|1b,0.000768,int8,cpu	|bm1684|	93%|	88.00%|	2227.91|	2.15|	5|	18|
|se7|	8%	| 4b,0.007178,int8,cpu|	1b,0.000467,int8,cpu|	bm1684x|	40%	|92%	|1671|	1.2|	5	|19|

## 技术资料

请通过算能官网[技术资料](https://developer.sophgo.com/site/index.html)获取相关文档、资料及视频教程。

## 社区

算能社区鼓励开发者多交流，共学习。开发者可以通过以下渠道进行交流和学习。

算能社区网站：https://www.sophgo.com/

算能开发者论坛：https://developer.sophgo.com/forum/index.html


## 贡献

欢迎参与贡献。更多详情，请参阅我们的[贡献者Wiki](./CONTRIBUTING_CN.md)。

## 许可证
[Apache License 2.0](./LICENSE)
