#(Hard)

bill = 20
tip_percentage = 0.15
tax_percentage = 0.067

tip = bill * tip_percentage
print(f"Tip: {tip}")

tax = bill * tax_percentage
print(f"Tax: {tax}")

total = bill + tip + tax
print(f"Total: {total}")
