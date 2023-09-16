def calculate(num1, num2, action):
    result = None
    match action:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num1 != 0:
                result = num1 / num2
            else:
                return "Can't divide by 0!"
    return result

if __name__ == "__main__":
    while True:
        while True:
            try:
                num1 = float(input("Give a first number:"))
                if isinstance(num1, float):
                    num2 = float(input("Give a second number:"))
                    break
            except ValueError:
                print("Invalid input. Please give a number!")
        action = input("Give a operator (+,-,*,/)")
        result = calculate(num1, num2, action)
        if result == "Can't devide by 0!":
            continue
        print(f"Your result is {result}")
        choice = input("Another calculation? (yes/no)")
        if choice == "yes":
            continue
        else:
            break
    print("Calculate again!")