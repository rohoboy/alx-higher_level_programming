#!/usr/bin/python3
"""Defines object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available."""
    return (dir(obj))
