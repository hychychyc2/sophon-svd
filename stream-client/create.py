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

# 定义请求体
data = {
    "TaskID": task_id,
    "InputSrc": {
        "SrcID": "600100000445030222",
        "StreamSrc": {
            "Address": "rtsp://172.26.13.17:8554/mystream"
        }
    },
    "Algorithm": [
        {
            "Type": int(Type),
            "TrackInterval": 1,
            "DetectInterval": 5,
            "TargetSize": {
                "MinDetect": 30,
                "MaxDetect": 250
            },
            # "DetectInfos": None,
            "DetectInfos": [
                {
                    "TripWire": {
                        "LineStart": {"X": 1000, "Y": 0},
                        "LineEnd": {"X": 1000, "Y": 1080},
                        "DirectStart": {"X": 170, "Y": 260},
                        "DirectEnd": {"X": 170, "Y": 260}
                    },
                    "HotArea": [
                        {"X": 10, "Y": 10},
                        {"X": 191, "Y": 10},
                        {"X": 191, "Y": 107},
                        {"X": 10, "Y": 107}
                    ]
                }
            ],
            "Extend": {"key": "value"}
        }
    ],
    "Reporting": {
        "ReportUrlList": ["http://172.18.0.123:9092/upload/data"]
    }
}

# 发送 POST 请求
response = requests.post(url, json=data, headers=headers)

# 打印响应内容
print(response.status_code)
print(response.text)
