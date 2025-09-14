subjects = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_subjects = sorted(subjects, key=lambda x: x[1])

print("Original list of tuples:", subjects)
print("Sorted list of tuples:", sorted_subjects)
