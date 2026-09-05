# Exercise 2
import time
temp=time.strftime("%H:%M:%S") # give current time in hours, minutes and seconds

if temp>="06:00:00" and temp<="12:00:00":
    print("Good Morning")
elif temp>="12:00:01" and temp<="17:00:00":
    print("Good Afternoon")
else:
    print("Good Evening")        