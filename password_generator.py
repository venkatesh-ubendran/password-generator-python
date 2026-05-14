
import random
import string

def check_strength(password):
    # strength = "Weak"

    if (len(password) >= 8 and
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in symbols for c in password)):
        strengths = "Strong"

    elif len(password) >= 6:
        strengths = "Medium"

    else:
        strengths = "weak";
   

    return strengths;

    


l = int(input("Number of letters: "))
s = int(input("Number of symbols: "))
n = int(input("Number of numbers: "))

if l == 0 and s == 0 and n == 0:
    print("Invalid input")
    exit()

letters = list(string.ascii_letters)
symbols = list("!@#$%^&*()")
numbers = list(string.digits)

password_list = []

for _ in range(l):
    password_list.append(random.choice(letters))

for _ in range(s):
    password_list.append(random.choice(symbols))

for _ in range(n):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = "".join(password_list)

strength = check_strength(password)

print("\nGenerated Password:", password)
print("Password Strength:", strength)
