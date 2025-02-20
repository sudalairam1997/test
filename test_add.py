import pytest
from add_numbers import add

def test_empty_string():
    assert add("") == 0

def test_single_number():
    assert add("1") == 1

def test_two_numbers():
    assert add("1,2") == 3

def test_multiple_numbers():
    assert add("1,2,3,4,5") == 15

def test_newline_delimiter():
    assert add("1\n2,3") == 6

def test_custom_delimiter():
    assert add("//;\n1;2") == 3

def test_custom_delimiter_pipe():
    assert add("//|\n1|2|3") == 6

def test_custom_multi_char_delimiter():
    assert add("//***\n1***2***3") == 6

def test_negative_number():
    with pytest.raises(ValueError, match="negative numbers not allowed -1"):
        add("-1,2,3")

def test_multiple_negative_numbers():
    with pytest.raises(ValueError, match="negative numbers not allowed -1,-2,-3"):
        add("-1,-2,-3")

def test_large_numbers():
    assert add("1,100,1000,10000") == 11101