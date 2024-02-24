import time
b = 0
start_time = time.time()
for i in range(0, 10000):
     b = b
end_time = time.time()
time_taken = end_time - start_time
print("time",time_taken)
print(start_time)