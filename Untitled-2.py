n1 = int(input("Enter the number: "))

for i in range(1, n1 + 1):  # Corrected 'for' loop with range()
    if n1 % i == 0:  # Properly indented 'if' statement
        a1 = n1 // i  # Compute the other factor using integer division
        print(f"Multiplication of {n1} = {i} * {a1}")
