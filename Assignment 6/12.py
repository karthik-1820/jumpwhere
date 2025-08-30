held=int(input("Enter the number of classes Held:"))
attended=int(input("Enter the number of classes attended:"))
perc=(attended/held)*100
print(f"percentage of class attended:{perc:.2f}%")
if perc>=75:
    print("Allowed to sit in the exam")
else:
    print("Not allowed")
