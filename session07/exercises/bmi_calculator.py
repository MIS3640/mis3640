import webbrowser


def calculate_bmi(weight, height):
    """
    return BMI based on weight (lb) and height (inch).
    """
    bmi = 703 * weight / (height * height)
    return bmi


def get_bmit_category():
    """
    Prompts user to input values for weight and height, converts them to
    floats, uses calculate_bmi to calculate BMI value, and prints the
    corresponding BMI category.
    """
    weight = input("Enter your weight (lb): ")
    height = input("Enter your height (inch): ")
    weight = float(weight)
    height = float(height)

    bmi = calculate_bmi(weight, height)

    if bmi <= 18.5:
        print(f"Your bmi is {bmi:.1f}. You are underweighted.")
        webbrowser.open("https://www.mcdonalds.com/us/en-us.html")
    # elif bmi > 18.5 and bmi <= 25:
    elif 18.5 < bmi <= 25:
        print(f"Your bmi is {bmi:.1f}. You are normal-weighted.")
    elif 25 < bmi < 30:
        print(f"Your bmi is {bmi:.1f}. You are overweighted.")
    else:
        print(f"Your bmi is {bmi:.1f}. You are obese.")


def main():
    get_bmit_category()


if __name__ == "__main__":
    get_bmit_category()
