def main():

    camel_case = input("camelCase: ")
    snake_case = ""

    for character in camel_case:

        if character.isupper():
            snake_case += "_" + character.lower()
        else:
            snake_case += character

    if snake_case.startswith("_"):
        snake_case = snake_case[1:]

    print("snake_case:", snake_case)


main()
