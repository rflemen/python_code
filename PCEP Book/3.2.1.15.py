c0 = int(input("Enter a number: "))
steps = 0

while c0 != 1:
    if c0 <= 0:
        print("You MUST enter a positive number!")
        break
    steps += 1
    if c0 % 2 == 0:
        c0 /= 2
        print(int(c0))
    else:
        c0 = (3 * c0) + 1
        print(int(c0))

print("Steps: ", steps)