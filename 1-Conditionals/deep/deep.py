# Ask user for answer
answer = (
    input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    .strip()
    .lower()
)

# Match it to Case
match answer:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No, it is 42")
