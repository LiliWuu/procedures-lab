"""
Utility procedures student implement and test.
"""

# This import is important later to understand what's going on
from typing import Dict, Optional

def add(a: float, b: float) -> float:
    """
    Return a + b.
    """
    # TODO: Implement
    
    return a + b

def fib(n: int) -> int:
    """
    Return the n-th Fibonacci number with fib(0) == 0, fib(1) == 1.
    """
    # TODO: implement
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fib(n-2) + fib(n-1)

"""
Simple "database"
Hi again! We imported `typing.Dict` because it's more readable type wise.
That is, so you can tell what we types of variables (string, integer, etc.) we want to use in our dictionary.
"""
_DB: Dict[str, Dict] = {}

def create_item(key: str, value: Dict) -> None:
    """
    Create or replace an item at key with value.
    """
    # TODO: implement
    _DB[key] = value

def read_item(key: str) -> Optional[Dict]:
    """
    Return the stored value or None if missing.
    """
    # TODO: implement
    if key in _DB:
        return _DB[key]
    else:
        return None

def update_item(key: str, patch: Dict) -> bool:
    """
    Update a stored dictionary item with the keys/values from path.
    Return True if item exists and was updated, False if item missing.
    """
    # TODO: implement
    if key in _DB:
        _DB[key].update(patch)
        return True
    else:
        return False


def delete_item(key: str) -> bool:
    """
    Delete item at key. Return True if deleted, False if item missing.
    """
    # TODO: implement
    if key in _DB:
       del _DB[key]
       return True
    else:
        return False 

def clear_db() -> None:
    """Helper for tests (remove all items)."""
    global _DB
    _DB = {}