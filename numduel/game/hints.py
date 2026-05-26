
# Hint system after half attempts are used

def show_hint(secret, no_of_attempts, max_attempts, hint_shown):
        
    if no_of_attempts > max_attempts / 2 and hint_shown == False:

        if secret % 2 == 0:
            print("Hint: Number is even")

        else:
            print("Hint: Number is Odd")

        if secret % 5 == 0:
            print("Hint: Number is divisible by 5")

        return True
    
    return False