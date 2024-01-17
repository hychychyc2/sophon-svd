#!/bin/bash

# 设置起始和结束的 id
start_id=$1
end_id=$2  # 例如，你的结束 id 是起始 id + 长度

# 循环执行 Python3 脚本
for ((id=start_id; id<=end_id; id++)); do
    python3 create.py $id 16
done