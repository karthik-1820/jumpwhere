import random

def generate_number():
    """Generate a random 4-digit number with non-repeated digits"""
    digits = list("0123456789")
    random.shuffle(digits)
   
    if digits[0] == '0':
        digits[0], digits[1] = digits[1], digits[0]
    return "".join(digits[:4])

def cows_and_bulls(secret, guess):
    """Return number of cows and bulls"""
    cows = sum(s == g for s, g in zip(secret, guess))
    bulls = sum((g in secret) for g in guess) - cows
    return cows, bulls

def main():
    print(" Welcome to the Cows and Bulls Game!")
    secret = generate_number()
    attempts = 0
    
    while True:
        guess = input("Enter a 4-digit number (digits must not repeat): ")
        
        if not guess.isdigit() or len(guess) != 4:
            print(" Invalid input! Please enter a 4-digit number.")
            continue
        if len(set(guess)) != 4:
            print("Digits must not repeat. Try again.")
            continue
        
        attempts += 1
        cows, bulls = cows_and_bulls(secret, guess)
        
        print(f"{cows} cows, {bulls} bulls")
        
        if cows == 4:
            print(f" Congratulations! You guessed the number {secret} in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
