#   <-- Input -->
n = int(input("Input any number"))
#   <-- List -->
hex_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
#   <-- Empty Content Holder -->
reversed_number = ""
#   <-- Loop -->
while n > 0:
    remainder = n % 16
    n -= remainder
    n //= 16
    #   <-- Turning it into a string and adding on to values. -->
    reversed_number += str(hex_values[remainder])
#   <-- Reversing the number -->
print(reversed_number[::-1])