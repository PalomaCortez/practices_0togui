## Cap 2 - Elementary Programing
##C2Ex2 Show current time

import time
#module in python with functions trelated to time predefined.

current_time = time.time() #get current time

#to obtain the total seconds since midnight 1/1/1970
total_seconds = int(current_time)

#to get the current second
current_second = total_seconds % 60

# to obtain the total minutes
total_minutes = total_seconds // 60

# to obtain the current minute
current_minute = total_minutes % 60

total_hours = total_minutes // 60

current_hour = total_hours % 24

# Display results
print("Current time is", current_hour, ":", current_minute, ":", current_second, "GMT")
