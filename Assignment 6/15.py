numbers = []
product = 1

while True:
    user = input("Enter an integer (press 'q' to quit): ")

    if user.lower() == 'q':
        break

    try:
        num = int(user)
        numbers.append(num)
        product *= num
    except ValueError:
        print("Invalid input, please enter an integer or 'q' to quit.")

if len(numbers) == 0:
    print("No numbers entered.")
else:
    avg = sum(numbers) / len(numbers)
    print("\nNumbers entered:", numbers)
    print(f"Average = {avg:.2f}")
    print(f"Product = {product}")
