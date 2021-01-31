from rich.console import Console

console = Console()
"""
Exercise 2
"""
# exercise 2.1
import math

r = 5
v = 4 / 3 * math.pi * r ** 3
console.print(f"The volume of a sphere with radius 5 is {v:.2f}.\n", style='bold')
# console.print()

# exercise 2.2
book_count = 60
price = 24.95
discount = 0.4
cost = price * (1 - discount) * book_count
shipping_cost_first = 3
shipping_cost_per = 0.75
shipping_cost = shipping_cost_first + shipping_cost_per * (book_count - 1)
total_cost = cost + shipping_cost
console.print(f"The total wholesale cost for {book_count} copies is ${total_cost:.2f}.")
console.print()

# exercise 2.3
start_time_hr = 6 + 52 / 60
easy_pace_hr = (8 + 15 / 60) / 60
tempo_pace_hr = (7 + 12 / 60) / 60
running_time_hr = 2 * easy_pace_hr + 3 * tempo_pace_hr
breakfast_hr = start_time_hr + running_time_hr
breakfast_min = (breakfast_hr - int(breakfast_hr)) * 60
breakfast_sec = (breakfast_min - int(breakfast_min)) * 60

console.print(
    f"Breakfast time is {int(breakfast_hr):02d}:{int(breakfast_min):02d}:{int(breakfast_sec):02d}."
)
console.print()

# exercise 2.4
perc = (89 - 82) / 82
console.print(f"The percentage of the increase is {perc*100:04.1f}%.")

# or
console.print(f"The percentage of the increase is {perc:05.1%}.")

console.print()
