#!/bin/bash

# 检查是否传入了参数 \$1
if [ -z $1 ]; then
    echo "Usage: bash add_algorithm.sh  <alrorithm>"
    exit 1
else
    echo "Parameter 1 is set to $1."
fi

# 你的其余脚本可以放在这里

alrorithm=$1
if [ -d "$alrorithm" ]; then
    echo "Directory $directory already exists."
else
    cp -r template $alrorithm
    mv $alrorithm/template.py $alrorithm/$alrorithm.py
fi

# 定义要替换的旧字符串和新字符串
old_string="template"
new_string="$alrorithm"

# 使用 sed 进行替换
sed -i "s/$old_string/$new_string/g" "$alrorithm/$alrorithm.py"
sed -i "s/$old_string/$new_string/g" "$alrorithm/config_logic.py"

# 输出结果
echo "Add $alrorithm success!"