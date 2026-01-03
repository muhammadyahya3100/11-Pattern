print("Welcome to floyd triangle pattern printing!")
row = int(input("Enter your row: "))
num = 1
print("~~~~~~🔺~~~~~~")
for i in range (1,1+row):
    for j in range (i):
        print(num, end=" ")
        num = num+1
    print()