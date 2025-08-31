class ParenthesesValidator:
    def __init__(self):
        self.pairs = {')': '(', '}': '{', ']': '['}

    def is_valid(self, s: str) -> bool:
        stack = []
        for char in s:
        
            if char in self.pairs:
                top = stack.pop() if stack else '#'
                if self.pairs[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
