# Exercise 3

import time


print(time.time())

current = time.time()
second = current % 60
minutes = (current // 60) % 60
hours = (current // 60) // 60 % 24
days = current // 60 // 60 // 24


print(
    f"Current time: {int(days):d} days, {int(hours):d} hours, {int(minutes):d} minutes and {second:.2f} seconds from Epoch."
)
