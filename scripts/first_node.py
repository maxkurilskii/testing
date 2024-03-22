#!/usr/bin/env python3

from datetime import datetime
current_time = datetime.now().strftime("%H:%M:%S")
next_time = current_time + 5
print("Текущее время:", current_time)
while(True):
 current_time = datetime.now().strftime("%H:%M:%S")
 if current_time == next_time:
   print("Текущее время:", current_time)
   next_time = current_time+10

