#'''
#  Noah Walton
#  IS 303 - A01

#  XP Calculator
#  This program estimates how many gaming sessions it would take to reach a certain level.
#  The user will input their current level, the target level, and the average XP earned per gaming session.

# Title
print("\nWelcome to the XP Calculator!\n")

# Inputs
current_xp = int(input("\nEnter your current XP: "))
target_xp = int(input("\nEnter the target XP: "))
xp_per_session = int(input("\nEnter the average XP earned per gaming session: "))

# Processes
sessions_needed = (target_xp - current_xp) / xp_per_session

# Outputs
print(f"\nTo reach your target XP of {target_xp} from your current XP of {current_xp}, you would need approximately {sessions_needed:.2f} gaming sessions at an average of {xp_per_session} XP per session.")
#'''