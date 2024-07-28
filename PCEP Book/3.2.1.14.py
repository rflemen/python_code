# Take the total number of blocks from user and convert it to integer
# Note: The input() function result is always a string
blocks = int(input("Enter the number of blocks: "))
# Initialize a variable counter which will count blocks used
counter=1
# Initialize a variable  height which will store the height of the pyramid
height=0

while counter <= blocks:
    height +=1
    counter +=height+1

print("The height of the pyramid:", height)