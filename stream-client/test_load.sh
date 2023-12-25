top -b -n 30  > cpu.log
rm tpu.log
bm-smi --file tpu.log & sleep 30 && kill $!
bash caculate.sh
# timeout -k 5 30s top -d 1 | grep "Cpu"  > cpu.log 
# timeout 30s bm-smi > tpu.log
# bash caculate.sh
