import requests
import json
import sys
# 定义请求的 URL
task_id=sys.argv[1]
Type=sys.argv[2]
print(task_id)
url = "http://0.0.0.0:8001/task/create"

# 定义请求头（如果有的话）
headers = {
    "Content-Type": "application/json"
}
# data={"TaskID":"1001","InputSrc":{"SrcID":"越线视频","StreamSrc":{"Address":"/workspace/sophon-stream/samples/tripwire/data/test.mp4"}},"Algorithm":[{"Type":1,"TrackInterval":1,"DetectInterval":5,"threshold":50,"TargetSize":{"MinDetect":30,"MaxDetect":250},"DetectInfos":[{"TripWire":{"LineStart":{"X":1145,"Y":531},"LineEnd":{"X":1728,"Y":927},"DirectStart":{"X":1436,"Y":729},"DirectEnd":{"X":1649,"Y":519}},"HotArea":[{"X":515,"Y":450},{"X":515,"Y":599},{"X":769,"Y":599},{"X":769,"Y":450}]}]}],"Reporting":{"ReportUrlList":["http://127.0.0.1:8089/api/upload"]}}
data={"TaskID":"1002","InputSrc":{"SrcID":"车牌","StreamSrc":{"Address":"/workspace/sophon-demo/application/VLPR/scripts/1080_1920_5s.mp4"}},"Algorithm":[{"Type":2,"TrackInterval":1,"DetectInterval":5,"threshold":50,"TargetSize":{"MinDetect":30,"MaxDetect":250},"DetectInfos":[{"TripWire":{"LineStart":{"X":0,"Y":0},"LineEnd":{"X":0,"Y":0},"DirectStart":{"X":0,"Y":0},"DirectEnd":{"X":0,"Y":0}},"HotArea":[{"X":792,"Y":89},{"X":89,"Y":312},{"X":164,"Y":742},{"X":1198,"Y":818},{"X":1810,"Y":453},{"X":1802,"Y":130}]}]}],"Reporting":{"ReportUrlList":["http://127.0.0.1:8089/api/upload"]}}
# 定义请求体
# data = {
#     "TaskID": task_id,
#     "InputSrc": {
#         "SrcID": "600100000445030222",
#         "StreamSrc": {
#             "Address": "rtsp://172.26.13.17:8554/mystream"
#         }
#     },
#     "Algorithm": [
#         {
#             "Type": int(Type),
#             "threshold": 50,
#             "TrackInterval": 1,
#             "DetectInterval": 5,
#             "TargetSize": {
#                 "MinDetect": 30,
#                 "MaxDetect": 250
#             },
#             # "DetectInfos": None,
#             "DetectInfos": [
#                 {
#                     "TripWire": {
#                         "LineStart": {"X": 1000, "Y": 0},
#                         "LineEnd": {"X": 1000, "Y": 1080},
#                         "DirectStart": {"X": 170, "Y": 260},
#                         "DirectEnd": {"X": 170, "Y": 260}
#                     },
#                     "HotArea": [
#                         {"X": 10, "Y": 10},
#                         {"X": 191, "Y": 10},
#                         {"X": 191, "Y": 107},
#                         {"X": 10, "Y": 107}
#                     ]
#                 }
#             ],
#             "Extend": {"key": "value"}
#         }
#     ],
#     "Reporting": {
#         "ReportUrlList": ["http://172.18.0.123:9092/upload/data"]
#     }
# }

# 发送 POST 请求
response = requests.post(url, json=data, headers=headers)

# 打印响应内容
print(response.status_code)
print(response.text)
