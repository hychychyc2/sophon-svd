grep "Cpu" "cpu.log" > a.log

cpu_u=$(awk '{sum += $2} END {print sum / NR}' a.log)
cpu_s=$(awk '{sum += $4} END {print sum / NR}' a.log)
tpu=$(awk '{
    match($0, /[0-9]+%/);
    if (RSTART) {
        value = substr($0, RSTART, RLENGTH - 1);
        gsub(/%/, "", value);
        sum += value;
        count++;
    }
} 
END {
    if (count > 0) {
        average = sum / count;
        print "Tpu Average:", average;
    } else {
        print "No values found.";
    }
}' tpu.log)

tpu_m=$(grep -oP '\b\d+MB/' tpu.log | awk -F'MB/' '{sum+=$1} END {print "Average: " sum/NR "MB/s"}'
)
# echo $cpu_s
# echo $cpu_u
cpu=$(echo "$cpu_s + $cpu_u" | bc)
echo "$cpu"
echo $tpu
echo $tpu_m