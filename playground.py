"""
One simluation:
use a var for total
repeat the following step N times:
        roll a dice, using random
        add the value to total
print out the total
    


Multiple Simulations:
# for i in range(10):

REpeat the following step 10 times:
    the simulation above
"""
import random


def simulation(n):
    """Run a simluation of rolling N dice, summing up the values and print"""
    total = 0
    for i in range(n):
        # total += random.randint(1, 6)
        total = total + random.randint(1, 6)
    print(total, total / n)


def multiple_simulations(m, n):
    """Run simluation M times"""
    for i in range(m):
        simulation(n)


def main():
    # simulation(100)
    multiple_simulations(10, 100_000)


if __name__ == "__main__":
    main()
