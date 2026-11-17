"""Dictionaries.

@see: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
@see: https://www.w3schools.com/python/python_dictionaries.asp

A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are
written with curly brackets, and they have keys and values.

Dictionaries are sometimes found in other languages as “associative memories” or “associative
arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by
keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used
as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object
either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since
lists can be modified in place using index assignments, slice assignments, or methods like append()
and extend().

It is best to think of a dictionary as a set of key: value pairs, with the requirement that the
keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}.
Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs
to the dictionary; this is also the way dictionaries are written on output.
"""

import pytest


def test_dictionary():
    """Dictionary"""

    fruits_dictionary = {
        'cherry': 'red',
        'apple': 'green',
        'banana': 'yellow',
    }

    assert isinstance(fruits_dictionary, dict)

    # You may access set elements by keys.
    assert fruits_dictionary['apple'] == 'green'
    assert fruits_dictionary['banana'] == 'yellow'
    assert fruits_dictionary['cherry'] == 'red'

    # To check whether a single key is in the dictionary, use the in keyword.
    assert 'apple' in fruits_dictionary
    assert 'pineapple' not in fruits_dictionary

    # Change the apple color to "red".
    fruits_dictionary['apple'] = 'red'

    # Add new key/value pair to the dictionary
    fruits_dictionary['pineapple'] = 'yellow'
    assert fruits_dictionary['pineapple'] == 'yellow'

    # Performing list(d) on a dictionary returns a list of all the keys used in the dictionary,
    # in insertion order (if you want it sorted, just use sorted(d) instead).
    assert list(fruits_dictionary) == ['cherry', 'apple', 'banana', 'pineapple']
    assert sorted(fruits_dictionary) == ['apple', 'banana', 'cherry', 'pineapple']

    # It is also possible to delete a key:value pair with del.
    del fruits_dictionary['pineapple']
    assert list(fruits_dictionary) == ['cherry', 'apple', 'banana']

    # The dict() constructor builds dictionaries directly from sequences of key-value pairs.
    dictionary_via_constructor = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

    assert dictionary_via_constructor['sape'] == 4139
    assert dictionary_via_constructor['guido'] == 4127
    assert dictionary_via_constructor['jack'] == 4098

    # In addition, dict comprehensions can be used to create dictionaries from arbitrary key
    # and value expressions:
    dictionary_via_expression = {x: x**2 for x in (2, 4, 6)}
    assert dictionary_via_expression[2] == 4
    assert dictionary_via_expression[4] == 16
    assert dictionary_via_expression[6] == 36

    # When the keys are simple strings, it is sometimes easier to specify pairs using
    # keyword arguments.
    dictionary_for_string_keys = dict(sape=4139, guido=4127, jack=4098)
    assert dictionary_for_string_keys['sape'] == 4139
    assert dictionary_for_string_keys['guido'] == 4127
    assert dictionary_for_string_keys['jack'] == 4098


def test_dictionary_retrieval():
    """Retrieving entries from a dictionary.

    Reading a missing key with square brackets raises a KeyError. The get() method is a safer
    alternative: it returns None, or a default value of your choice, when the key is missing.
    """

    stock = {'apples': 10, 'bananas': 0, 'cherries': 25}

    # Square brackets raise a KeyError when the key does not exist.
    with pytest.raises(KeyError):
        stock['mangoes']  # pylint: disable=pointless-statement

    # get() returns None for a missing key instead of raising an error.
    assert stock.get('mangoes') is None

    # The second argument of get() is the default value returned for a missing key.
    assert stock.get('mangoes', 0) == 0

    # The default is only used when the key is missing, not when the stored value is 0.
    assert stock.get('bananas', 100) == 0

    # keys(), values() and items() give access to the content of the dictionary.
    assert list(stock.keys()) == ['apples', 'bananas', 'cherries']
    assert list(stock.values()) == [10, 0, 25]
    assert list(stock.items()) == [('apples', 10), ('bananas', 0), ('cherries', 25)]

    # items() is handy for looping over keys and values at the same time.
    in_stock = []
    for fruit, quantity in stock.items():
        if quantity > 0:
            in_stock.append(fruit)
    assert in_stock == ['apples', 'cherries']


def test_dictionary_update_and_remove():
    """Updating and removing dictionary entries.

    The update() method adds or overwrites several entries at once. The pop() method removes a key
    and returns its value, while popitem() removes and returns the most recently added pair.
    """

    grades = {'Alice': 85, 'Bob': 72}

    # update() overwrites the value of an existing key and adds the keys that are new.
    grades.update({'Bob': 78, 'Carol': 91})
    assert grades == {'Alice': 85, 'Bob': 78, 'Carol': 91}

    # setdefault() adds the key only if it is missing, then returns the value stored for it.
    assert grades.setdefault('Dave', 60) == 60
    assert grades.setdefault('Alice', 0) == 85  # Alice already has a grade, so it is kept
    assert grades == {'Alice': 85, 'Bob': 78, 'Carol': 91, 'Dave': 60}

    # pop() removes a key and returns its value.
    assert grades.pop('Dave') == 60
    assert 'Dave' not in grades

    # pop() raises a KeyError for a missing key, unless a default value is given.
    assert grades.pop('Eve', None) is None
    with pytest.raises(KeyError):
        grades.pop('Eve')

    # popitem() removes and returns the last key/value pair that was inserted.
    assert grades.popitem() == ('Carol', 91)
    assert grades == {'Alice': 85, 'Bob': 78}

    # clear() removes every entry. An empty dictionary is "falsy" in a condition.
    grades.clear()
    assert not grades
