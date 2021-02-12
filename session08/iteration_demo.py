def sum_all():
    """Calculate sum of integers from 0 to 10 and print the result"""
    current_sum = 0

    for i in range(1, 1001):
        print(f'Iteration {i}:')
        print(f'The value of i is {i}')
        current_sum = current_sum + i
        print(f'After adding, the sum is {current_sum}.')
        print()

    print(f'The final result is {current_sum}.')


def sum_odd():
    """Calculate the sum of odd numbers from 1 to 1000, and print the sum"""
    current_sum = 0

    # for i in range(1, 1001):
    #     print(f'Iteration {i}:')

    #     if i % 2 == 1:  # check if i is an odd number
    #         print(f'The value of i is {i}')
    #         current_sum = current_sum + i
    #         print(f'After adding the odd number, the sum is {current_sum}.')

    #     print()

    for i in range(1, 1001, 2):
        print(f'The value of i is {i}')
        current_sum = current_sum + i
        print(f'Currently, the sum is {current_sum}.')
        print()

    print(f'The final result is {current_sum}.')


def main():
    # sum_all()
    sum_odd()


if __name__ == "__main__":
    main()
