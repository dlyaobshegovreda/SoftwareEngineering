import time
from datetime import datetime

duration = 5

for i in range(duration):
    current_time = datetime.now()
    print("Текущее время:", current_time)

    time.sleep(1)