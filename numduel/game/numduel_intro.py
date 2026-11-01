#!/usr/bin/env python3
"""NUMDUEL — cinematic lockdown intro."""

import os
import sys
import time

# Enable ANSI colors on Windows
os.system("")

TTY = sys.stdout.isatty()

# ───────────────────── COLORS ─────────────────────
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"

WIDTH = 46


# ───────────────────── HELPERS ─────────────────────
def pause(seconds):
    """Pause animations only when running in a terminal."""
    if TTY:
        time.sleep(seconds)


def clear_screen():
    """Clear the terminal screen."""
    if TTY:
        print("\033[2J\033[H", end="")


def typed(text, delay=0.03, color=""):
    """Print text with a typing effect."""
    if not TTY:
        print(f"{color}{text}{RESET}")
        return

    sys.stdout.write(color)

    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)

    print(RESET)


def make_box(lines, color=MAGENTA):
    """Create a double-line terminal box."""
    box_lines = [
        f"{color}╔{'═' * WIDTH}╗{RESET}"
    ]

    for line in lines:
        if line == "-":
            box_lines.append(
                f"{color}╠{'═' * WIDTH}╣{RESET}"
            )

        elif isinstance(line, tuple):
            text = line[1].center(WIDTH)
            box_lines.append(
                f"{color}║{RESET}{text}{color}║{RESET}"
            )

        else:
            text = ("  " + line).ljust(WIDTH)
            box_lines.append(
                f"{color}║{RESET}{text}{color}║{RESET}"
            )

    box_lines.append(
        f"{color}╚{'═' * WIDTH}╝{RESET}"
    )

    return box_lines


# ───────────────────── CORE SCREEN ─────────────────────
def core_screen():
    """Build the NumDuel core-access screen."""
    return [
        "",
        ("center", "N U M D U E L      //      CORE ACCESS"),
        "",
        "-",
        "CONNECTION ESTABLISHED",
        "TARGET VALUE: [ CLASSIFIED ]",
        "ACCESS ATTEMPTS: LIMITED",
        "SHIELDS: ■ ■ ■ ■ ■",
        "",
        "Find the value. Avoid system lockout.",
    ]


# ───────────────────── LOCKDOWN INTRO ─────────────────────
def intro_lockdown():
    """Display the cinematic lockdown intro."""

    # Flashing breach warning
    if TTY:
        for index in range(8):
            clear_screen()

            warning_color = MAGENTA if index % 2 == 0 else CYAN

            warning = (
                f"{warning_color}{BOLD}"
                f"{'!! BREACH DETECTED !!'.center(WIDTH + 2)}"
                f"{RESET}"
            )

            print(warning)

            # Magenta frame, cyan system information
            for line in make_box(core_screen(), MAGENTA):
                line = line.replace(
                    "CONNECTION ESTABLISHED",
                    f"{CYAN}CONNECTION ESTABLISHED{MAGENTA}"
                )
                line = line.replace(
                    "TARGET VALUE: [ CLASSIFIED ]",
                    f"{CYAN}TARGET VALUE: [ CLASSIFIED ]{MAGENTA}"
                )
                line = line.replace(
                    "ACCESS ATTEMPTS: LIMITED",
                    f"{CYAN}ACCESS ATTEMPTS: LIMITED{MAGENTA}"
                )
                line = line.replace(
                    "SHIELDS: ■ ■ ■ ■ ■",
                    f"{CYAN}SHIELDS: ■ ■ ■ ■ ■{MAGENTA}"
                )

                print(line)

            sys.stdout.write("\a")
            sys.stdout.flush()
            time.sleep(0.2)

        clear_screen()

    # Final stable screen
    print(
        f"{MAGENTA}{BOLD}"
        f"{'!! BREACH DETECTED !!'.center(WIDTH + 2)}"
        f"{RESET}"
    )

    for line in make_box(core_screen(), MAGENTA):
        print(line)

    print()

    # Cyan lockdown countdown
    for number in (3, 2, 1):
        typed(
            f"   LOCKDOWN IN {number}...",
            0.03,
            CYAN + BOLD
        )
        pause(0.5)

    print()

    # Final messages
    typed(
        "   LOCKDOWN ABORTED.",
        0.04,
        WHITE + BOLD
    )

    typed(
        "   THE CORE IS LETTING YOU IN.",
        0.04,
        MAGENTA + BOLD
    )

    print()


# ───────────────────── RUN ─────────────────────
if __name__ == "__main__":
    intro_lockdown()
    print(RESET)