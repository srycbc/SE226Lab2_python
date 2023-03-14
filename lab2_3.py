x = int(input("Please enter a number between 3 and 9:"))

for i in range(x):
    for j in range(i+1):
        print("* ", end="")
    print("\n")

for i in range(x-1, 0, -1):
    for j in range(i):
        print("* ", end="")
    print("\n")








