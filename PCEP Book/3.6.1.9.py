my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = [] # The helping list inside which we will add only unique numbers

for i in my_list:
    if i not in new_list: # The comparison part
        new_list.append(i) # Only unique numbers will be added. Duplicates won't.
# To update the original list. Or, you can print the new_list instead.
my_list = new_list

print("The list with unique elements only:")
print(my_list)