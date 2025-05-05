# Author: Deniz
# program that calculates the discriminant (Δ) using the formula Δ = b^2 - 4ac

# asks the user to enter values for a, b, and c
a = float(input("Enter the value of a: "))  # Stores the value of 'a'
b = float(input("Enter the value of b: "))  # Stores the value of 'b'
c = float(input("Enter the value of c: "))  # Stores the value of 'c'

# calculates the discriminant using the formula
delta = b**2 - 4*a*c  # calculates b squared minus 4 times a times c

# prints the result
print(f"The discriminant (Δ) value is: {delta}")  # displays the answer
