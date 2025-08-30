total = 0
count = 0

print("Enter integers (0 to stop):")

while True:
    num = int(input())
    if num == 0:
        break
    total += num
    count += 1

if count == 0:
    print("No numbers were entered.")
else:
    average = total / count
    print("Sum =", total)
    print("Average =", average)
