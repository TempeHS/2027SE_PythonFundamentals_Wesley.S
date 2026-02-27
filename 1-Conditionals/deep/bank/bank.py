# Prompt greeting
greeting = input("Greeting: ").strip().lower()

# Check the greeting
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
