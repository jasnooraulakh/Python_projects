import time

h_time = int(time.strftime("%H"))
# Convert the time to integer for if else

if h_time < 12:
    print("Good Morning!")
elif 12 < h_time < 16:
    print("Good Afternoon")
else:
    print("Good Evening")

timestamp = time.strftime("%H:%M:%S")
print(f"The time is {timestamp}")
# print the actual time after greetings
