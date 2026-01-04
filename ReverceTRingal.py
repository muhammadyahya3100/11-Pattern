row = int(input("Enter the number of rows: "))
print("~~~~~~🔻~~~~~~")

space = row - 1

for i in range(1, row + 1):
   
    for j in range(space):
        print(" ", end="")

   
    for j in range(i):
        print("*", end="")

    print()
    space -= 1
