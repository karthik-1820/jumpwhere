class TwoSum:
    def find_pair(self, numbers, target):
        num_dict = {}
        for i, num in enumerate(numbers):
            if target - num in num_dict:
                return num_dict[target - num], i
            num_dict[num] = i

two_sum = TwoSum()
numbers = [2, 7, 11, 15]
target = 9

result = two_sum.find_pair(numbers, target)
print("Indices:", result)
print("Numbers:", numbers[result[0]], "+", numbers[result[1]])
