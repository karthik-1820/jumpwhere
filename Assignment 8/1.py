class RomanConverter:
    def __init__(self):
        
        self.roman_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        self.value_map = {sym: val for val, sym in self.roman_map}

    def int_to_roman(self, num: int) -> str:
        """Convert integer to Roman numeral."""
        roman = ""
        for val, sym in self.roman_map:
            while num >= val:
                roman += sym
                num -= val
        return roman

    def roman_to_int(self, roman: str) -> int:
        """Convert Roman numeral to integer."""
        i = 0
        num = 0
        while i < len(roman):

            if i + 1 < len(roman) and roman[i:i+2] in self.value_map:
                num += self.value_map[roman[i:i+2]]
                i += 2
            else:
                num += self.value_map[roman[i]]
                i += 1
        return num

converter = RomanConverter()

print(converter.int_to_roman(1994))  
print(converter.int_to_roman(58))   

print(converter.roman_to_int("MCMXCIV"))  
print(converter.roman_to_int("LVIII"))
