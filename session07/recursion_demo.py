def f():
    print('Hi')
    f()


# f()


def countdown(n):
    import time

    time.sleep(1)

    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n)


# countdown(5)
