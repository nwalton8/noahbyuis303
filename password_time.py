#'''
#  Noah Walton
#  IS 303 - A01

#  Password Cracking Time Estimator
#  This program calculates the time it would take to crack a password
#  This program is estimating it for someone using a brute force attack method.

# Title
print("\nPassword Cracking Time Estimator!\n")

# Inputs
username = input("\nEnter the username: ")
password_length = int(input("\nEnter the password length: "))
character_set_size = int(input("\nEnter the character set size (e.g., 26 for lowercase letters, 52 for \
upper and lowercase, 62 for letters and digits, etc.): "))
attempts_per_second = 1000000000  # Assuming 1 billion attempts per second

# Processes
total_combinations = character_set_size ** password_length
cracking_time_seconds = total_combinations / attempts_per_second

# Outputs
print(f"\n\nAlright {username}, it would take approximately {cracking_time_seconds} seconds to crack your password.")
print(f"That's with a password of length {password_length} and a character set size of {character_set_size}.")
#'''