
#!/usr/bin/python3

import unittest

import pytest
from pytest import raises
from hamcrest import *

import keycodes


@pytest.mark.parametrize("in_put, out_put", [
    ("a", 30),
    ("s", 31),
    ("1", 2),
    ("A", [42, 30]),
    ("!", [42, 2]),
    ("Home", 102),
    ("F12", 88),
    ("ESCAPE", 1)
])
def test_item_to_evdev(in_put, out_put):
    assert out_put == keycodes.item_to_evdev(in_put)

# @pytest.mark.parametrize("string", ["","aa", "a "])
# def test_char_to_evdev_raises_length(string):
    # with pytest.raises(ValueError):
        # keycodes.char_to_evdev(string)

@pytest.mark.parametrize("items, result" ,[
    (["a", "A", "1", "!", "Home", "F12", "ESCAPE"],
     [30, [42, 30], 2, [42, 2], 102, 88, 1]),
])
def test_list_to_evdev(items, result):
    assert result == keycodes.list_to_evdev(items)

def test_str_to_evdev():
    pass

