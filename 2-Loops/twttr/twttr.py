def main():
    text = input("Enter Text: ")

    print("Output: ", end="")
    for char in text:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            print(char, end="")
    print()


if __name__ == "__main__":
    main()
