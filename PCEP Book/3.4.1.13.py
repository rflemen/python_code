beatles = []
# step 1
print("Step 1:", beatles)

# step 2
beatles.append("John")
beatles.append("Paul")
beatles.append("George")
print("Step 2:", beatles)

# step 3
for i in range(2):
    beatles.append(input("Enter a beatle: "))
    i += 1
print("Step 3:", beatles)

# step 4
del beatles[3]
del beatles[3]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
