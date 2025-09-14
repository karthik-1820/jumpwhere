total = 0

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    total += num

avg = total / 10

print(f"Average of the 10 numbers: {avg:.2f}")
