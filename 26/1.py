file = open("26/26_1.txt")
line = int(file.readline())
start = 1633305600
end = start + 604800
count = 0
time_pr = [0 for i in range(0, 604801)]
for i in file:
    start_pr, end_pr = i.split()
    if (int(start_pr) < start) and ((int(end_pr) > start) or (int(end_pr) == 0)):
        count+=1
    if (int(start_pr) >= start) and (int(start_pr) <= end):
        time_pr[int(start_pr) - start] = time_pr[int(start_pr) - start] + 1
    if (int(end_pr) >= start) and (int(end_pr) <= end):
        time_pr[int(end_pr) - start] = time_pr[int(end_pr) - start] - 1
sum_time = 0
max_process = 0
for i in range(1, 604801):
    count +=time_pr[i]
    if count > max_process:
        max_process = count
        sum_time = 0
    if count == max_process:
        sum_time += 1
print(max_process, sum_time)
    
