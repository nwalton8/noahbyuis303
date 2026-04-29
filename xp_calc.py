#'''
#  Noah Walton
#  IS 303 - A01

#  XP Calculator
#  This program estimates how many gaming sessions it would take to reach a certain level.
#  The user will input their current level, the target level, and the average XP earned per gaming session.

# Inputs
player_name = input("\nEnter your player name: ")
current_xp = float(input("\nEnter your current XP: "))
target_xp = float(input("\nEnter the target XP: "))
xp_per_session = float(input("\nEnter the average XP earned per gaming session: "))

# Processes
sessions_needed = (target_xp - current_xp) / xp_per_session

# Outputs
print(f"\n{player_name}, to reach your target XP of {target_xp} from your current XP of {current_xp}, you would need approximately {sessions_needed} gaming sessions at an average of {xp_per_session} XP per session.")
#'''