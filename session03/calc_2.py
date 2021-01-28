"""
Exercise 2
"""
# exercise 2.1
import math

r = 5
v = 4 / 3 * math.pi * r ** 3
print(f"The volume of a sphere with radius 5 is {v:.2f}.")
print()

# erercise 2.2
cost = (24.95 - 24.95 * 0.40) * 60 + 3 + 0.75 * (60 - 1)
print(f"The total wholesale cost for 60 copies is ${cost:.2f}.")
print()

# exercise 2.3
start_time_hr = 6 + 52 / 60
easy_pace_hr = (8 + 15 / 60) / 60
tempo_pace_hr = (7 + 12 / 60) / 60
running_time_hr = 2 * easy_pace_hr + 3 * tempo_pace_hr
breakfast_hr = start_time_hr + running_time_hr
breakfast_min = (breakfast_hr - int(breakfast_hr)) * 60
breakfast_sec = (breakfast_min - int(breakfast_min)) * 60

print(
    f"Breakfast time is {int(breakfast_hr):02d}:{int(breakfast_min):02d}:{int(breakfast_sec):02d}."
)
print()

# exercise 2.4
perc = (89 - 82) / 82 * 100
print(f"The percentage of the increase is {perc:04.1f}%.")
print()
