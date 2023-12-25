import requests
import sys

# 定义请求的 URL
url = "http://0.0.0.0:8001/task/list"

# 定义请求头（如果有的话）
headers = {
    "Content-Type": "application/json"
}

# 定义请求体
data = {
}

# 发送 POST 请求
response = requests.post(url, json=data, headers=headers)

# 打印响应内容
print(response.status_code)
print(response.text)
