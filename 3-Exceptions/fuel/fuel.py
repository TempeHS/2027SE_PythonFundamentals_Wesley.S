while True:
    fraction = input("Fraction: ")
    try:
        x_str, y_str = fraction.split("/")
        x = int(x_str)
        y = int(y_str)

        if x > y:
            continue

        percentage = round((x / y) * 100)

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        break

    except (ValueError, ZeroDivisionError):
        pass
