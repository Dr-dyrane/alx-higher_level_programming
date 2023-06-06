#!/usr/bin/python3
"""
Defines a locked class that prevents the user from dynamically
creating new instance attributes.
"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes,
    except for 'first_name'.
    """

    __slots__ = ["first_name"]
