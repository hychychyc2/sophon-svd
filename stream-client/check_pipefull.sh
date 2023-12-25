#!/bin/bash
id=1
# rm -rf ../sophon-stream/samples/build/*log
monitor_path="/data/stream/sophon-stream/samples/build"
file_suffix="stream.log"  # 以指定字符串为后缀的文件
target_string="DataPipe is full"  # 要检查的目标字符串
exitt(){
    exit 1
}
while true;do
    # python3 post2.py $id 
    # sleep 30
    # top -b -n 30  > cpu.log
    # cpu=$(bash caculate.sh)
    # echo $cpu
    find "$monitor_path" -type f -name "*$file_suffix" -print | while read -r file_path; do
        # 检查文件是否包含目标字符串
        if grep -q "$target_string" "$file_path"; then
            # echo $id
            # python3 ctrol.py $id 
            echo "File '$file_path' contains the target string."
            sleep 30000000000

            top -b -n 30  > cpu.log
            rm tpu.log
            nohup bm-smi --file tpu.log > /dev/null 2>&1 & sleep 3 && kill $! 
            bash caculate.sh
            exitt
        fi
        
    done
    ((id++))
done
# # 遍历文件夹
# for file_path in "$folder_path"/*."$file_suffix"; do
#     # 检查文件是否存在
#     echo $file_path
#     if [ -e "$file_path" ]; then
#         # 读取文件内容并检查是否包含目标字符串
#         if grep -q "$target_string" "$file_path"; then
#             echo "File '$file_path' contains the target string."
#         fi
#     fi
# done
