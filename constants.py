"""
For a project this small, there's no real need to have this in a separate file.
However in any real project, having a centralized constants file is a good idea.
"""


class Stacks:
    """I would typically use Enums here, but for a toy app like this, it's overly complex"""

    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"
