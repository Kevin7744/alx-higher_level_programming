#!/usr/bin/python3
"""
My list module
"""


class MyList(list):
    """
    Class that inherits from list
    """
    def print_sorted(self):
        """
        prints sorted list
        """
        print(sorted(self.copy()))
