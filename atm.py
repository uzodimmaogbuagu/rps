# Set the actual correct PIN for the account
CORRECT_PIN = 12345
# comment
# Initialise the pin_state variable to 0
pin_state = 0

# Track the number of attempts made
attempts = 0

# Keep looping until a valid PIN is entered AND attempts are less than 3
while pin_state == 0 and attempts < 3:
    # Use a try/except block to catch non-number inputs (letters/symbols)
    try:
        # Ask the customer for input and convert it to an integer
        pin_choice = int(input("Enter your 4-digit PIN: "))
        
        # Increment the attempt counter immediately after input
        attempts += 1

        # Check if the PIN is outside the permitted 4-digit range
        if pin_choice < 1000 or pin_choice > 9999:
            print("Invalid PIN length. Must be 4 digits. Please try again.")
        
        # Check if the 4-digit PIN is actually correct
        elif pin_choice != CORRECT_PIN:
            print("Incorrect PIN. Please try again.")
            
        else:
            # PIN is valid and correct
            pin_state = pin_choice

# This is a value error            
    except ValueError:
        # This runs if the user types letters instead of numbers
        print("Invalid input. Please enter numbers only.")
        attempts += 1 # Counts as a failed attempt

# Code executes here once the loop ends (either success or max attempts reached)
if pin_state != 0:
    print("\nAccount unlocked.")
    print(f"Number of attempts made: {attempts}")
else:
    print("\nATM access blocked.")





































# # Initialise the pin_state variable to 0
# pin_state = 0

# # Keep looping until pin_state holds a valid PIN (between 1000 and 9999)
# while pin_state < 9999 or pin_state >=9999:
#     # Ask the customer for input and convert it to an integer
#     pin_choice = int(input("Enter your 4-digit PIN: "))
    
#     # Check if the PIN is outside the permitted range
#     if pin_choice < 1000 or pin_choice > 9999:
#         print("Invalid PIN. Please try again.")
#     else:
#         pin_state = pin_choice

# # Code executes here once the loop condition becomes false
# print("Account unlocked. After successful validation")
