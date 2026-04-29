# My first Python program
# IS 303 - Build 1

print("Welcome to IS 303!")
print("Let's learn to program.")

# Interactive greeting program
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to IS 303.")

# Tip Calculator
# Takes a meal total and calculates tips at different percentages

meal_total = float(input("What was your meal total? $"))

tip_15 = meal_total * 0.15
tip_18 = meal_total * 0.18
tip_20 = meal_total * 0.20

print(f"\nTip options for a ${meal_total:.2f} meal:")
print(f"  15% tip: ${tip_15:.2f}")
print(f"  18% tip: ${tip_18:.2f}")
print(f"  20% tip: ${tip_20:.2f}")
print(f"  Total with 18% tip: ${meal_total + tip_18:.2f}")

