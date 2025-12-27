secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
user_guess = 0

while user_guess != secret_number:
    user_guess = int(input("Enter your guess: "))
    if user_guess == secret_number:
        print("Well done, muggle! You are free now.")
    else:
        print("Ha ha! You're stuck in my loop!")