"""
hints.py

Responsible for generating hints based on:
- Secret number
- Attempts used
- Maximum attempts
- Whether hints have already been shown

Returns hints instead of printing them.
"""

def show_hint(secret, no_of_attempts, max_attempts, hint_shown):
    """
    Returns:
        (hint_shown, hints)

    hint_shown -> bool
    hints -> list of strings
    """

    if hint_shown:
        return True, []

    if no_of_attempts <= max_attempts / 2:
        return False, []

    hints = []

    # Even / Odd hint
    if secret % 2 == 0:
        hints.append("Hint: Number is even")
    else:
        hints.append("Hint: Number is odd")

    # Divisibility hint
    if secret % 5 == 0:
        hints.append("Hint: Number is divisible by 5")

    return True, hints