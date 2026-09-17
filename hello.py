import platform
import random
import time

print("Hello world")
print("Node OS:", platform.system(), platform.machine())

for i in range(6):
    temp = round(random.uniform(24.0, 32.0), 1)  # 模擬溫度
    status = "ALERT" if temp > 30 else "ok"
    print(f"[{i}] temp = {temp} C  {status}")
    time.sleep(1)


h = round(random.uniform(40.0, 80.0), 1)  # 模擬溫度
print(f"h = {h} C  {status}")
