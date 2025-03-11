"""
Thoughts:
  for a simple function like this, my work here is pretty over-engineered.
  I did it this way to "showcase my proficiency".
  However, in a real-world scenario, I would have just written the function and moved on.
  Though a function like this in the real world would much more likely be a method in a class.
  In that case I would have had logging and error handling in the higher level methods calling this function.
  and my tests would have more likely focused around that class.
"""

from typing import Any, Optional
from constants import Stacks


def sort(width: int, height: int, length: int, mass: int) -> str:
    """
    return string according to these rules:
    STANDARD: standard packages (those that are not bulky or heavy) can be handled normally.
    SPECIAL: packages that are either heavy or bulky can't be handled automatically.
    REJECTED: packages that are both heavy and bulky are rejected.
    """
    try:
        match (is_bulky(width, height, length), is_heavy(mass)):
            case (False, False):
                return Stacks.STANDARD
            case (True, True):
                return Stacks.REJECTED
            case (True, False) | (
                False,
                True,
            ):  # this could also be `case _:` but I like to be explicit
                return Stacks.SPECIAL
    except TypeError:
        # duck typing is more pythonic than checking types ahead of time,
        # but depending on how this fucntion would be used in a real world scenario
        # it might be better to pre-check the types of the arguments
        # or not to catch the TypeError at all
        # if pre-checking I would probably use a decorator or switch to using something like pydantic
        width = coerce(width)
        height = coerce(height)
        length = coerce(length)
        mass = coerce(mass)
        if any((width is None, height is None, length is None, mass is None)):
            return Stacks.REJECTED
        return sort(width, height, length, mass)


def coerce(value: Any) -> Optional[int]:
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def is_bulky(width: int, height: int, length: int) -> bool:
    """
    determine if a package with the given dimensions is bulky
    A package is bulky if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³
    or when one of its dimensions is greater or equal to 150 cm.
    """
    if width >= 150 or height >= 150 or length >= 150:
        return True
    if width * height * length >= 1_000_000:
        return True
    return False


def is_heavy(mass: int) -> bool:
    """A package is heavy when its mass is greater or equal to 20 kg."""
    return mass >= 20


if __name__ == "__main__":
    while True:
        out = sort(
            input("Enter width: "),
            input("Enter height: "),
            input("Enter length: "),
            input("Enter mass: "),
        )
        print(f"result: {out}")