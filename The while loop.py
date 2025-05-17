print("The half Pyramid patern of hashtags")
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    j = 1
    while j <= i:
        print("#", end=" ")
        j += 1
    print()