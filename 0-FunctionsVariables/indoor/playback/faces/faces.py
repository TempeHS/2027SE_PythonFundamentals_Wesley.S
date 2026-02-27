def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


def main():
    user_input = input("enter text: ")

    result = convert(user_input)
    print(result)


if __name__ == "__main__":
    main()
