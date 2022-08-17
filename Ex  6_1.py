# Example 6_1
def sum_number():
    sum = 0;
    for n in range(1, 11):
        if (n%2 == 0):
            sum += n
    print(f"sum of 1 .. 10 = {sum}")

print("Program sum 1 bto 10 used function.")
sum_number()

