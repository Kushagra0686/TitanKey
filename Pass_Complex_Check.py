"""Interactive Password Complexity Checker By KUSHAGRA VERMA"""
# Importing Required Modules
import pyperclip
import string
import random
# Function For Determination of Complexity Score
#####################################################################################
def complexity(password):
    length = len(password)
    has_upper = any(char in  string.ascii_uppercase for char in password)
    has_lower = any(char in string.ascii_lowercase for char in password)
    has_digit = any(char in string.digits for char in password)
    has_special = any(char in string.punctuation for char in password)
    #Check For Common Wordlist
    with open('common.txt','r') as f:
        common = f.read().splitlines()
    # Flag for Score
    complexity_score = 0
    if password in common :
        print(f"\033[1;91;40m Password Found In A Common Wordlist -> Strength: \033[1;31;40m[=>\t\t\t\t\t\t ] 0.0%\033[m")
        print()
        print("\033[1;93;40mRun The Script Again to Check for Different Passwords...\033[m")
        exit()
    if length >= 16:
        complexity_score += 1
    if has_upper:
        complexity_score += 1
    if has_lower:
        complexity_score += 1
    if has_digit:
        complexity_score += 1
    if has_special:
        complexity_score += 1
    # Returning The Score (MAX = 6)
    return complexity_score
#####################################################################################
# Check for Strength
def strength(password):
    complexity_score = complexity(password)
    # checking for score for strength
    if complexity_score == 5 :
        strength_perc = calculate_percentage(complexity_score,5)
        time_req='Around 100 Billion to 93 Trillion Years .....'
        print("--" * 25)
        print(" \033[1;92;40m----Password is Strong---\033[m ")
        print()
        print(f" Strength : \033[1;32;40m[=================================> {round(strength_perc,2)}%\033[m]")
        print()
        print(f"Time Required To Brute Force This Category : \033[1;92;40m{time_req}\033[m")
        print()
        print("--" * 25)
    elif complexity_score >= 3:
        strength_perc = calculate_percentage(complexity_score, 5)
        time_req=''
        if len(password)>=16:
            time_req='Around 800K years ...'
        else:
            time_req="Around 51 years to 200 years ..."
        print("--" * 25)
        print(" \033[1;94;40m----Password has medium strength----\033[m")
        print()
        print(f" Strength : \033[1;93;40m[===================>\t\t ] {round(strength_perc,2)}%\033[m")
        print()
        print(f"Time Required To Brute Force This Category : \033[1;96;40m{time_req}\033[m")
        print()
        generate_pass = input("Do You Want an Improved Password Randomly Generated ?? ('y' for YES / 'n' for NO ) :\t")
        #
        print()
        if generate_pass == 'y':
            print("--" * 25)
            generate(password)
            print()
        else:
            print()
            print("\033[1;31;40m--------- Exiting ---------\033[m")
            print("--" * 25)
            exit()

    else:
        strength_perc = calculate_percentage(complexity_score, 5)
        time_req='Around 25 seconds to 1 Day'
        print("--" * 25)
        print(" \033[1;91;40m----Password is Weak---- \033[m")
        print()
        print(f" Strength : \033[1;31;40m[====>\t\t\t\t] {round(strength_perc,2)}%\033[m")
        print()
        print(f"Time Required To Brute Force This Category : \033[1;91;40m{time_req}\033[m")
        print()
        generate_pass = input("Do You Want a Strong Password Randomly Generated ?? ('y' for YES / 'n' for NO ) : ").lower()
        print()
        if generate_pass == 'y':
            print("--" * 25)
            generate(password)
            print()
        #
        else:
            print()
            print("\033[1;31;40m--------- Exiting ---------\033[m")
            print("--" * 25)
            exit()

#####################################################################################
# Determining Strength Percentage W.R.T Total Score
def calculate_percentage(part, whole):
    return (part / whole) * 100

# Generate Strong Random Password for Medium and Weak Tests
def generate(existing_password):
    max_length = random.randint(16, 24)
    while len(existing_password) < max_length:
        # Choose a random position to insert the character
        insert_pos = random.randint(0, len(existing_password))
        # Generate a random character
        random_char = random.choice(string.ascii_letters + string.digits + string.punctuation)
        # Insert the random character into the existing password at the chosen position
        existing_password = existing_password[:insert_pos] + random_char + existing_password[insert_pos:]
    # Ensure the password is no longer than 32 characters
    score = 5
    strength_perc = calculate_percentage(score,5)
    print("--" * 25)
    print(f"\033[1;96;40mImproved Password :\033[m \033[1;93;40m{existing_password[:32]}\033[m")
    print()
    print(f" Strength : \033[1;32;40m[=================================> {round(strength_perc,2)}%\033[m]")
    print()
    print(f"Time Required To Brute Force This Category : \033[1;92;40mAround 100 Billion to 93 Trillion Years .....\033[m")
    print()
    copy_ch = input(
        "Do You Want Your New Password To Be Copied To CLipboard ('y' for YES / 'n' for NO ) :\t").lower()
    if copy_ch == 'y':
        pyperclip.copy(existing_password[:32])
        print()
        print("\033[1;96;40m-*-*-*--Copied Successfully--*-*-*-\033[m")
        print("--" * 25)
    else:
        print("--" * 25)
        print("\033[1;31;40m--------- Exiting ---------\033[m")
        exit()

#

#####################################################################################
# Create the main input field in terminal
print("--"*50)
print('''\033[1;91;40m
$$$$$$$$\ $$\   $$\                         $$\   $$\                    
\__$$  __|\__|  $$ |                        $$ | $$  |                   
   $$ |   $$\ $$$$$$\    $$$$$$\  $$$$$$$\  $$ |$$  / $$$$$$\  $$\   $$\ 
   $$ |   $$ |\_$$  _|   \____$$\ $$  __$$\ $$$$$  / $$  __$$\ $$ |  $$ |
   $$ |   $$ |  $$ |     $$$$$$$ |$$ |  $$ |$$  $$<  $$$$$$$$ |$$ |  $$ |
   $$ |   $$ |  $$ |$$\ $$  __$$ |$$ |  $$ |$$ |\$$\ $$   ____|$$ |  $$ |
   $$ |   $$ |  \$$$$  |\$$$$$$$ |$$ |  $$ |$$ | \$$\\$$$$$$$\ \$$$$$$$ |
   \__|   \__|   \____/  \_______|\__|  \__|\__|  \__|\_______| \____$$ |
                                                               $$\   $$ |
                                                               \$$$$$$  |
                                                                \______/                                                                             
--By KUSHAGRA VERMA--
\033[m''')
print()
print("\033[1;92;40mUltimate Password Complexity Checker With Password Strengthening Functionality !! \033[m")
print()
password = input("Enter The Password to Check (Min. 4 Characters & Max. 32 Characters) : ")
print()
if len(password) > 32 or len(password) < 4:
    print("\033[1;31;40mUsage : Password Must Be in Range of 4 to 32 characters\033[m\t")
else:
    print(f" Password Length :\t \033[1;35;40m{len(password)}\033[m")
    print()
    strength(password)
print("--"*50)
# END OF PROGRAM
# Signing Off __ KV


