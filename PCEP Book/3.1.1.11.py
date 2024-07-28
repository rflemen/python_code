income = float(input("Enter the annual income: "))
#
# Write your code here.
#
if income <= 85528:
    tax = (income*.18) - 556.02
    if tax < 0:
        tax = 0
elif income > 85528:
    tax = 14839.02 + (income - 85528)*.32

tax = round(tax, 0)
print("The tax is:", tax, "thalers")