def check_fermat(a, b, c, n):
    """Check if Fermat's theorem holds. Print depending on the check result."""
    assert n > 2
    if a ** n + b ** n == c ** n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work.')


def check_fermat_with_inputs():
    """Prompts user to input 4 integers and check weather Fermat's theorem holds."""
    print('Please enter 4 integers for a, b, c and n to check Fermat\'s theorem:')
    a = int(input("Please enter an integer for a: "))
    b = int(input("Please enter an integer for b: "))
    c = int(input("Please enter an integer for c: "))
    n = int(input("Please enter an integer (>2) for n: "))

    check_fermat(a, b, c, n)


def main():
    check_fermat_with_inputs()


if __name__ == "__main__":
    main()
