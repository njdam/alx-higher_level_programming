#!/usr/bin/python3
"""A file with a function to find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """A function to find a peak in a list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return (list_of_integers[0])
